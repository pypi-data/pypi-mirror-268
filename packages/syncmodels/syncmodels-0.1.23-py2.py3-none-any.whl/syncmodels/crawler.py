"""
Asyncio Crawler Support
"""

import asyncio
from asyncio.queues import Queue
import queue
import re
import os
import sys
import traceback
from typing import List, Dict, Any, Callable
import yaml

import aiohttp


from agptools.helpers import expandpath
from agptools.progress import Progress
from agptools.containers import walk, myassign, rebuild, SEP, list_of

from syncmodels.syncmodels import SyncModel

# ---------------------------------------------------------
# Loggers
# ---------------------------------------------------------
from agptools.logs import logger

log = logger(__name__)


# ---------------------------------------------------------
# Parallel Crawler Support
# ---------------------------------------------------------
class iAgent:
    "the minimal interface for an agent in crawler module"

    def __init__(self, config_path=None, name="", include=None, exclude=None):
        self.name = name
        # tasks to be included or excluded
        self.include = include or [".*"]
        self.exclude = exclude or []

        self.progress = Progress()

        if not config_path:
            config_path = "config.yaml"
        config_path = expandpath(config_path)
        self.root = os.path.dirname(config_path)
        self.stats_path = os.path.join(self.root, "stats.yaml")

        if not config_path:
            config_path = "config.yaml"
        config_path = expandpath(config_path)

        try:
            with open(config_path, "rt", encoding="utf-8") as f:
                self.cfg = yaml.load(f, Loader=yaml.Loader)
        except Exception:
            self.cfg = {}

    async def run(self):
        "agent's initial setup"
        await self._create_resources()
        await self.bootstrap()

    async def bootstrap(self):
        "Add the initial tasks to be executed by crawler"
        log.info(">> [%s] entering bootstrap()", self.name)

        for func, args, kwargs in self._bootstrap():
            log.info("+ [%s] %s(%s, %s)", self.name, func, args, kwargs)
            self.add_task(func, *args, **kwargs)
        log.info("<< [%s] exit bootstrap()", self.name)

    # async def bootstrap(self):
    # "Add the initial tasks to be executed by crawler"

    def _bootstrap(self):
        "Provide the initial tasks to ignite the process"
        return []

    def add_task(self, func, *args, **kw):
        "add a new pending task to be executed by this iAgent"
        raise NotImplementedError()

    async def _create_resources(self):
        "create/start the agent's resources needed before starting"

    async def _stop_resources(self):
        "stop/release the agent's resources on exit"


class iBot(iAgent):
    "Interface for a bot"
    MAX_QUEUE = 200

    def __init__(self, result_queue: Queue, *args, **kw):
        super().__init__(*args, **kw)
        self.result_queue = result_queue
        self.fiber = None
        self.task_queue = asyncio.queues.Queue()
        self._wip = []

    def add_task(self, func, *args, **kw):
        "add a new pending task to be executed by this iBot"
        universe = list(kw.values()) + list(args)

        def check():
            for string in universe:
                string = str(string)
                for pattern in self.include:
                    if re.match(pattern, string):
                        return True
                for pattern in self.exclude:
                    if re.match(pattern, string):
                        return False

        if check():
            self.task_queue.put_nowait((func, args, kw))

    async def run(self):
        "the entry point / main loop of a single `fiber` in pool"

        log.info(">> [%s] entering run()", self.name)
        await super().run()

        while True:
            try:
                while (pending := self.result_queue.qsize()) > self.MAX_QUEUE:
                    print(
                        f"Pause worker due too much results pending in queue: {pending}"
                    )
                    await asyncio.sleep(1)

                # Get a task from the queue
                task = await asyncio.wait_for(self.task_queue.get(), timeout=5)
                if task is None:
                    break  # Break the loop
                self._wip.append(1)
                func, args, kwargs = task
                # print(f">> Processing task: {args}: {kwargs}")
                if isinstance(func, str):
                    func = getattr(self, func)
                assert isinstance(func, Callable)
                async for data in func(*args, **kwargs):
                    item = task, data
                    await self.result_queue.put(item)
                self._wip.pop()
                # print(f"<< Processing task: {func}")
            except queue.Empty:
                pass
            except asyncio.exceptions.TimeoutError:
                pass
            except Exception as why:
                log.error(why)
                log.error("".join(traceback.format_exception(*sys.exc_info())))

        log.info("<< [%s] exit run()", self.name)

    async def dispatch(self, task, data, *args, **kw):
        "do nothing"
        log.info(" - dispacht: %s: %s ; %s, %s", task, data, args, kw)

    def remain_tasks(self):
        "compute how many pending tasks still remains"
        return len(self._wip) + self.task_queue.qsize()


class HTTPBot(iBot):
    "Basic HTTPBot"

    async def get_data(self, kind, path, **kwargs):
        """
        Example a crawling function for Plancrawler crawler.

        Get data related to the given kind and path.
        May add more tasks to be done by crawler.

        """
        real_kind = kind.split("-")[0]  # may be separated by '-'
        holder = getattr(self.model, real_kind, None)
        if holder is None:
            log.warning("model hasn't attribute: '%s'", real_kind)
            return

        query_data = {
            "limit": 50,
            "offset": 0,
        }
        query_data.update(kwargs)
        extra = self._extract_path_info(kind, path)

        # call delegate method to gather the information from 3rd system
        result = await self._get_data(path, query_data)
        if not result:
            return

        for org in result:
            data = {**org, **extra}
            data = self._clean(kind, data)
            uid = self.get_uid(kind, data)

            # restruct data internally, based on RESTRUCT_DATA rules
            reveal = build_paths(data)
            try:
                data = self._restruct(kind, data, reveal)
            except Exception as why:
                print(why)

            # more complex data transformations
            data = self._transform(kind, data)

            # bless data with some additional tags
            tags = self.tagger.retag(kind, data, reveal)
            data[TAG_KEY] = tags  # TODO: review used key...

            data = overlap(holder.setdefault(uid, {}), data)

            # give data to crawler
            yield data, (kind, uid, org)

            # to be nice with other fibers
            # await asyncio.sleep(0)

            # get nested items (if any)
            # I'd rather NESTED_URL to be explicitly filled
            # (i.e NESTED_URL[kind]) instead use NESTED_URL.get(kind)
            # in order to check if there's missing some data for an item
            # in the remote system
            for sub_kind, sub_url in self.NESTED_URL[kind]:
                sub_url = sub_url.format_map(data)
                self.add_task(self.get_data, sub_kind, sub_url)

        if kind in self.PAGINATION_KIND:
            if not query_data["offset"]:  # 1st time
                # request all pagination at once!
                while query_data["offset"] < meta["count"]:
                    query_data = dict(query_data)
                    query_data["offset"] += query_data["limit"]
                    kwargs = {
                        **kwargs,
                        **{
                            "kind": kind,
                            "path": path,
                        },
                        **query_data,
                    }

                    self.add_task(
                        self.get_data,
                        **kwargs,
                    )

            # params['offset'] = (page := page + len(result))

    async def _get_data(self, path, query_data):
        "A helper method to get the data from external system"

        log.info(" >  %s.get_data (%s ; %s)", self.name, path, query_data)

        for tries in range(1, 15):
            try:
                async with aiohttp.ClientSession() as session:
                    # log.info(f"{self.app_url}{path}: {query_data}")
                    async with session.get(
                        f"{self.app_url}{path}", params=query_data
                    ) as response:
                        if response.status in (200,):
                            result = await response.json()
                            meta = result["meta"]
                            result = result["result"]
                            return result
                        elif response.status in (400,):
                            log.error("%s: %s: %s", response.status, path, query_data)
                            result = await response.json()
                            log.error(result)
                            return
                        else:
                            log.error("Status: %s", response.status)
            except Exception as why:
                log.error(why)
                log.error("".join(traceback.format_exception(*sys.exc_info())))

            log.warning("retry: %s: %s, %s", tries, path, query_data)
            await asyncio.sleep(0.5)


class iCrawler(iAgent):
    "Interface for a crawler"
    bots: Dict[Any, iBot]

    def __init__(self, syncmodel: SyncModel, raw_storage=None, *args, **kw):
        super().__init__(*args, **kw)
        self.bot = {}
        self.round_robin = []

        self.result_queue = Queue()

        self.stats = {}
        self.show_stats = True

        self.syncmodel = list_of(syncmodel, SyncModel)
        self.raw_storage = raw_storage

    async def run(self) -> bool:
        """TBD"""
        await super().run()

    def add_task(self, func: str, *args, **kw):
        "add a new pending task to be executed by this iBot"
        universe = list(kw.values()) + list(args)

        if not self.round_robin:
            self.round_robin = list(self.bot.values())

        while self.round_robin:
            bot = self.round_robin.pop()
            bot.add_task(func, *args, **kw)
            break

    def remain_tasks(self):
        "compute how many pending tasks still remains"
        n = self.result_queue.qsize()
        for bot in self.bot.values():
            n += bot.remain_tasks()
        return n


class iAsyncCrawler(iCrawler):
    """A crawler that uses asyncio"""

    # need to be redefined by subclass
    MODEL = None
    BOT = HTTPBot

    # governance data
    MAPPERS = {}
    RESTRUCT_DATA = {}
    RETAG_DATA = {}
    REFERENCE_MATCHES = []
    KINDS_UID = {}

    def __init__(self, fibers=3, *args, **kw):
        super().__init__(*args, **kw)
        self.fibers = fibers
        self.t0 = 0
        self.t1 = 0
        self.nice = 300
        self.model = self.MODEL()

    async def run(self) -> bool:
        """Execute a full crawling loop"""
        await super().run()

        # Create a worker pool with a specified number of 'fibers'
        self.t0 = time.time()
        self.t1 = self.t0 + self.nice

        # wait until all work is done
        while remain := self.remain_tasks():
            try:
                # result = await asyncio.wait_for(self.result_queue.get(), timeout=2)
                # result = await self.result_queue.get()
                result = await asyncio.wait_for(self.result_queue.get(), timeout=2)
                res = await self.dispatch(*result)
                if not res:
                    log.warning("Can't save item in storage: %s", result[0][2])
                    log.warning("%s", pformat(result[1]))
                    foo = 1
            except queue.Empty:
                pass
            except asyncio.exceptions.TimeoutError:
                pass
            except Exception as why:
                log.error(why)
                log.error("".join(traceback.format_exception(*sys.exc_info())))

            self.progress.update(
                remain=remain,
                stats=self.stats,
            )

        await self._stop_resources()
        result = all([await sync.save() for sync in self.syncmodel])
        return result

    async def dispatch(self, task, data, *args, **kw):
        "create an item from data and try to update into storage"
        func, _args, _kw = task
        # _kw: {'kind': 'groups', 'path': '/groups?statistics=true'}
        # data:  {'id': 104, ... }
        kind = _kw["kind"]
        # uid = self.get_uid(kind, data)

        data, (kind, uid, org) = data

        # inject item into models
        item = self.new(kind, data)

        # result = await self.syncmodel.put(item)
        result = all([await sync.put(item) for sync in self.syncmodel])

        # save original item if a raw storage has been specified
        if self.raw_storage:
            fqid = item.id
            await self.raw_storage.put(fqid, org)

        # check if we need to do something from time to time
        t1 = time.time()
        if t1 > self.t1:
            self.t1 = t1 + self.nice
            await self.save(nice=True)

        return result

    async def save(self, nice=False):
        log.info("Saving models")
        all([await sync.save(nice=nice) for sync in self.syncmodel])
        if self.raw_storage:
            await self.raw_storage.save(nice=nice)

    async def _create_resources(self):
        loop = asyncio.get_running_loop()
        for n in range(self.fibers):
            name = f"bot-{n}"
            bot = self.BOT(result_queue=self.result_queue, name=name)
            self.bot[name] = bot
            bot.fiber = loop.create_task(bot.run())

    async def _stop_resources(self):
        # Add sentinel values to signal worker threads to exit
        for nane, bot in self.bot.items():
            bot.task_queue.put_nowait(None)

        # Wait for all worker threads to complete
        # for worker in self.workers:
        # worker.join()

    async def _get_url(self, path, query_data) -> List:
        raise NotImplementedError()

    def get_uid(self, kind, data):
        "Try to guess the `uid` of an item of `type_` class"
        if kind in self.KINDS_UID:
            uid_key, func, id_key = self.KINDS_UID[kind]
            # uid_key = self.KINDS_UID.get(kind, '{id}')
            if not isinstance(data, dict):
                data = data.model_dump_json()
            uid = uid_key.format_map(data)
            # uid = item[uid]
            fquid = func(uid)
            data[id_key] = fquid
            data["_fquid"] = fquid
            data["_uid"] = uid
        else:
            uid = data["id"]
        return uid

    def convert_into_references(self, data):
        """Search for nested objects in `value` and convert them into references"""
        if self.REFERENCE_MATCHES:
            id_keys = list(
                walk(
                    data,
                    keys_included=self.REFERENCE_MATCHES,
                    include_struct=False,
                )
            )
            for idkey, idval in id_keys:
                # myassign(value, myget(value, idkey), idkey[:-1])
                myassign(data, idval, idkey[:-1])

        return data

    def new(self, kind, data):
        """Try to create / update an item of `type_` class from raw data

        - convert nested data into references
        - convert data to suit pydantic schema
        - get the pydantic item

        """
        data2 = self.convert_into_references(data)
        klass = self.MAPPERS.get(kind)
        if not klass:
            log.warning("missing MAPPERS[%s] class!", kind)
            return

        item = klass.pydantic(data2)
        return item

    def remain_tasks(self):
        "compute how many pending tasks still remains"
        n = sum([sync.running() for sync in self.syncmodel])
        if self.raw_storage:
            n += self.raw_storage.running()
        n += super().remain_tasks()
        return n

    def _clean(self, kind, data):
        for k, v in data.items():
            if isinstance(v, str):
                data[k] = v.strip()
        return data

    def _restruct(self, kind, data, reveal):
        """Restructure internal data according to `RESTRUCT_DATA` structure info.

        Finally the result is the overlay of the original `data` and the restructured one.
        """
        restruct = {}
        info = self.RESTRUCT_DATA.get("default", {})
        info.update(self.RESTRUCT_DATA.get(kind, {}))
        for path, value in reveal.items():
            for pattern, (new_path, new_value) in info.items():
                m = re.match(pattern, path)
                if m:
                    d = m.groupdict()
                    d["value"] = value
                    key = tuple(new_path.format_map(d).split(SEP))
                    _value = value if new_value == COPY else new_value.format_map(d)
                    restruct[key] = _value

        # build the restructured data
        restruct = rebuild(restruct, result={})
        # create the overlay of both data to be used (possibly) by pydantic
        data = {**data, **restruct}

        return data

    def _transform(self, kind, data):
        return data

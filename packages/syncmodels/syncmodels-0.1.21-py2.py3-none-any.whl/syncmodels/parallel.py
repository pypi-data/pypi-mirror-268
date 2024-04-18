import asyncio
import os
import re
import random
import sys
import traceback
from typing import List
import yaml
from pprint import pformat

# ---------------------------------------------------------
# concurrent data gathering
import concurrent.futures
import threading
import multiprocessing
import queue
import time

# ---------------------------------------------------------


from .helpers import expandpath
from .syncmodels import SyncModel, COPY

# ---------------------------------------------------------
# Loggers
# ---------------------------------------------------------
from agptools.containers import walk, myassign, rebuild, SEP, list_of
from agptools.logs import logger
from agptools.progress import Progress

log = logger(__name__)


def nop(*args, **kw):
    pass


async def anop(*args, **kw):
    yield None


class Parallel:
    def __init__(self, num_threads=3, dispatch=None):
        self.num_threads = num_threads
        self.task_queue = queue.Queue()
        self.result_queue = queue.Queue()
        self._wip = []
        self.show_stats = True
        self.dispatch = dispatch or nop

        self.workers = []
        self.pool = None

    def bootstrap(self):
        self.pool = multiprocessing.Pool(processes=self.num_threads)

    def _create_executor_pool(self):
        if True:
            self.workers = [
                threading.Thread(target=self.worker) for _ in range(self.num_threads)
            ]

            for worker in self.workers:
                worker.start()

        else:
            self.worker = multiprocessing.Pool(processes=self.num_threads)

    def _stop_executor_pool(self):
        # Add sentinel values to signal worker threads to exit
        for _ in range(self.num_threads):
            self.task_queue.put(None)

        # Wait for all worker threads to complete
        for worker in self.workers:
            worker.join()

    def run(self):
        self.t0 = time.time()
        self.elapsed = 0.0

        # Create a thread pool with a specified number of threads
        self._create_executor_pool()
        # Start worker threads

        # wait until all work is done
        shows = 0
        while remain := self.remain_tasks():
            try:
                result = self.result_queue.get(timeout=1)
                self.dispatch(*result)
            except queue.Empty as why:
                foo = 1

            shows -= 1
            if self.show_stats and shows <= 0:
                log.warning(f"remain tasks: {remain} : {self.num_threads} threads")
                shows = 50
            # time.sleep(0.25)
            self.elapsed = time.time() - self.t0

        self._stop_executor_pool()

    def add_task(self, func, *args, **kw):
        self.task_queue.put_nowait((func, args, kw))

    def remain_tasks(self):
        return (
            len(self._wip) + len(self.task_queue.queue) + len(self.result_queue.queue)
        )

    def worker(self):
        while True:
            try:
                # Get a task from the queue
                task = self.task_queue.get(block=True, timeout=1)
                if task is None:
                    break  # Break the loop
                self._wip.append(1)
                func, args, kwargs = task
                # print(f">> Processing task: {func}")
                result = func(*args, **kwargs)
                item = task, result
                self.result_queue.put(item)
                self._wip.pop()
                # print(f"<< Processing task: {func}")
            except queue.Empty:
                pass


class AsyncParallel:
    def __init__(self, num_threads=3, dispatch=None):
        self.num_threads = num_threads
        self.task_queue = asyncio.queues.Queue()
        self.result_queue = asyncio.queues.Queue()
        self._wip = []
        self.show_stats = True
        self.dispatch = dispatch or anop

        self.workers = []  # tasks
        # self.pool = None
        self.loop = None

    def bootstrap(self):
        "Provide the initial tasks to ignite the process"
        # self.pool = multiprocessing.Pool(processes=self.num_threads)

    async def _create_executor_pool(self):

        self.workers = [
            self.loop.create_task(self.worker(), name=f"worker-{n}")
            for n in range(self.num_threads)
        ]

    async def _stop_executor_pool(self):
        # Add sentinel values to signal worker threads to exit
        for _ in range(self.num_threads):
            self.task_queue.put_nowait(None)

        # Wait for all worker threads to complete
        # for worker in self.workers:
        # worker.join()

    async def run(self):
        self.t0 = time.time()
        self.elapsed = 0.0
        self.loop = asyncio.get_running_loop()

        # Create a worker pool with a specified number of 'fibers'
        await self._create_executor_pool()

        # wait until all work is done
        last = 0
        while remain := self.remain_tasks():
            try:
                # result = await asyncio.wait_for(self.result_queue.get(), timeout=2)
                result = await self.result_queue.get()
                await self.dispatch(*result)
            except queue.Empty as why:
                foo = 1
            except asyncio.exceptions.TimeoutError as why:
                foo = 1

            t1 = time.time()
            self.elapsed = t1 - self.t0
            # print("foo")
            if self.show_stats and t1 - last > 10:
                log.info(f"remain tasks: {remain} : {self.num_threads} fibers")
                last = t1
            # time.sleep(0.25)

        await self._stop_executor_pool()

    def add_task(self, func, *args, **kw):
        self.task_queue.put_nowait((func, args, kw))

    def remain_tasks(self):
        return len(self._wip) + self.task_queue.qsize() + self.result_queue.qsize()

    async def worker(self):
        while True:
            try:
                # Get a task from the queue
                while remaining := self.remain_tasks() < 1000:
                    print(f"Pause worker due too much remainin task: {remaining}")
                    await asyncio.sleep(1)
                    foo = 1
                task = await asyncio.wait_for(self.task_queue.get(), timeout=2)
                if task is None:
                    break  # Break the loop
                self._wip.append(1)
                func, args, kwargs = task
                # print(f">> Processing task: {args}: {kwargs}")
                result = await func(*args, **kwargs)
                item = task, result
                self.result_queue.put_nowait(item)
                self._wip.pop()
                # print(f"<< Processing task: {func}")
            except queue.Empty:
                foo = 1
            except asyncio.exceptions.TimeoutError as why:
                foo = 1
            except Exception as why:
                log.error(why)
                log.error("".join(traceback.format_exception(*sys.exc_info())))
                foo = 1
                print(tb)
                foo = 1


class iCrawler:
    "Interface for a crawler"

    def __init__(self, config_path=None, include=None, exclude=None):
        # tasks to be included or excluded
        self.include = include or ['.*']
        self.exclude = exclude or []
        
        self.progress = Progress()
        self.task_queue = asyncio.queues.Queue()
        self.result_queue = asyncio.queues.Queue()
        self._wip = []

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

    def _bootstrap(self):
        "Provide the initial tasks to ignite the process"

    async def bootstrap(self):
        "Add the initial tasks to be executed by crawler"
        for func, args, kwargs in self._bootstrap():
            self.add_task(func, *args, **kwargs)

    def add_task(self, func, *args, **kw):
        "add a new pending task to be executed by crawler"
        # TODO: >> remove debug / faster deep
        #if random.random() < 0.75:
            #return
        # TODO: << remove debug / faster deep
        
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

    def remain_tasks(self):
        "compute how many pending tasks still remains"
        return len(self._wip) + self.task_queue.qsize() + self.result_queue.qsize()

    async def dispatch(self, task, data, *args, **kw):
        "do nothing"


class AsyncCrawler(iCrawler):
    """A crawler that uses asyncio"""

    MAPPERS = {}
    RESTRUCT_DATA = {}
    RETAG_DATA = {}
    REFERENCE_MATCHES = []
    KINDS_UID = {}

    def __init__(self, syncmodel: SyncModel, raw_storage=None, fibers=3, *args, **kw):
        super().__init__(*args, **kw)
        self.fibers = fibers
        self.show_stats = True
        self.stats = {}
        self.workers = []  # tasks
        self.loop = None
        self.t0 = 0
        self.t1 = 0
        self.nice = 300

        self.syncmodel = list_of(syncmodel, SyncModel)
        self.raw_storage = raw_storage

    async def _create_pool(self):
        self.workers = [
            self.loop.create_task(self.worker(), name=f"worker-{n}")
            for n in range(self.fibers)
        ]

    async def _stop_pool(self):
        # Add sentinel values to signal worker threads to exit
        for _ in range(self.fibers):
            self.task_queue.put_nowait(None)

        # Wait for all worker threads to complete
        # for worker in self.workers:
        # worker.join()

    async def run(self) -> bool:
        """Execute a full crawling loop"""
        self.loop = asyncio.get_running_loop()

        # Create a worker pool with a specified number of 'fibers'
        self.t0 = time.time()
        self.t1 = self.t0 + self.nice
        await self._create_pool()

        await self.bootstrap()

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

        await self._stop_pool()
        result = all([await sync.save() for sync in self.syncmodel])
        return result

    async def worker(self):
        "the main loop of a single `fiber`"
        while True:
            try:
                while (pending := self.result_queue.qsize()) > 200:
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
                foo = 1

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

    async def save(self, nice=False):
        log.info("Saving models")
        all([await sync.save(nice=nice) for sync in self.syncmodel])
        if self.raw_storage:
            await self.raw_storage.save(nice=nice)
    
        
    def remain_tasks(self):
        "compute how many pending tasks still remains"
        n = sum([ sync.running() for sync in self.syncmodel])
        if self.raw_storage:
            n += self.raw_storage.running()
        n += super().remain_tasks()
        return n
        
        
    async def _get_data(self, path, query_data) -> List:
        raise NotImplementedError()

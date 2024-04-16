# ----------------------------------------------------------
# Storage Port
# ----------------------------------------------------------
import os
import pickle
import re
import time
import threading
from multiprocessing import Process
import yaml

# from surrealdb import Surreal
from surrealist import Surreal as Surrealist

from .helpers import expandpath

# ---------------------------------------------------------
# Loggers
# ---------------------------------------------------------

from agptools.logs import logger
from agptools.helpers import parse_uri, build_uri

log = logger(__name__)

from .model import BaseModel

#REGEXP_FQUI = re.compile(r"((?P<ns>[^/]*?)/)?(?P<table>[^:]+):(?P<uid>.*)$")
def split_fqui(fqid):
    try:
        table, uid = fqid.split(":")
        return table, uid
    except ValueError:
        return fqid, None


class iCRUD:

    async def create(self, item):
        "TBD"

    async def read(self, fqid):
        "alias for get"
        return await self.get(fqid)

    async def update(self, fqid, item):
        "TBD"

    async def delete(self, fqid):
        "TBD"

    async def put(self, fqid, data) -> bool:
        "Try to create / update an item of `type_` class from raw data"

    async def list(self):
        "TBD"

    async def count(self):
        "TBD"

    async def exists(self, fqid):
        "TBD"

    async def get(self, fqid, kind=None) -> BaseModel | None:
        "TBD"
        pass

    async def set(self, fqid, data, merge=False):
        "TBD"
        return False

    async def put(self, fqid, data) -> bool:
        return await self.set(fqid, data)

    async def get_all(self):
        "TBD"

    async def set_all(self, items):
        "TBD"

    async def delete_all(self):
        "TBD"

    async def exists_all(self, uids):
        "TBD"

    async def get_many(self, uids):
        "TBD"

    async def set_many(self, uids, items):
        "TBD"

    async def delete_many(self, uids):
        "TBD"

    async def exists_many(self, uids):
        "TBD"

    async def save(self, nice=False):
        "TBD"


class Storage(iCRUD):
    def __init__(self, url):
        self.url = url
        self.background = []
        
    def running(self):
        self.background = [p for p in self.background if p.is_alive()]
        return len(self.background)
    
    async def info(self):
        raise NotImplementedError()


class StoragePort(Storage):
    PATH_TEMPLATE = "{self.url}/{table}"

    def __init__(self, url="./db"):
        super().__init__(url=url)
        url = expandpath(url)
        os.makedirs(url, exist_ok=True)
        self.url = url
        self.cache = {}


    def _file(self, table):
        return self.PATH_TEMPLATE.format_map(locals())

    def _load(self, table, force=False):
        universe = self.cache.get(table)
        if force or universe is None:
            path = self._file(table)
            if os.path.exists(path):
                try:
                    universe = self._real_load(path)
                except Exception as why:
                    log.warning(why)
            if universe is None:
                universe = {}                
            self.cache[table] = universe
        return universe

    def _save(self, table, universe=None, pause=0):
        if universe is None:
            universe = self._load(table)
        path = self._file(table)
        self._real_save(path, universe, pause=pause)
        return universe

    def _real_load(self, path):
        raise NotImplementedError()

    def _real_save(self, path, universe, pause=0):
        raise NotImplementedError()

    async def get(self, fqid, query=None, **params):
        table, uid = split_fqui(fqid)
        universe = self._load(table)
        if query:
            raise NotImplementedError

        data = universe.get(fqid, {})
        return data

    async def set(self, fqid, data, merge=False):
        table, uid = split_fqui(fqid)
        universe = self._load(table)
        if merge:
            data0 = await self.get(fqid)
            # data = {** data0, ** data} # TODO: is faster?
            data0.update(data)
            data = data0

        universe[fqid] = data
        return True

    async def save(self, table=None,  nice=False):
        table = table or list(self.cache)
        if not isinstance(table, list):
            table = [table]
        for i, tab in enumerate(table):
            log.debug("[%s]: [%s] saving: %s", self.__class__.__name__, i, tab)
            pause = i if nice else 0
            self._save(tab, pause=pause+0.1)

    async def info(self, ns=''):
        "Returns storage info: *tables*, etc"
        if ns:
            table = f"{ns}/.*"
        else:
            table = f".*"
            
        pattern = self._file(table=table)
        top = os.path.dirname(pattern)
        for root, _, files in os.walk(top):
            for file in files:
                path = os.path.join(root, file)
                m = re.match(pattern, path)
                if m:
                    relpath = os.path.relpath(path, self.url)
                    name = os.path.splitext(relpath)[0]
                    yield name


class PickleStorage(StoragePort):
    PATH_TEMPLATE = "{self.url}/{table}.pickle"

    def __init__(self, url="./db"):
        super().__init__(url)

    def _real_load(self, path):
        try:
            universe = pickle.load(open(path, "rb"))
        except Exception as why:
            log.error("%s: Error loading: %s: %s", self, path, why)
            universe = {}
        return universe

    def _real_save(self, path, universe, pause=0):
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            pickle.dump(universe, open(path, "wb"))
        except Exception as why:
            log.error("%s: Error savig: %s: %s", self, path, why)


class YamlStorage(StoragePort):
    PATH_TEMPLATE = "{self.url}/{table}.yaml"

    def __init__(self, url="./db"):
        super().__init__(url)
        self.lock = 0

    def _real_load(self, path):
        try:
            universe = yaml.load(open(path, encoding="utf-8"), Loader=yaml.Loader)
        except Exception as why:
            log.error("%s: Error loading: %s: %s", self, path, why)
            universe = {}
        return universe

    def _real_save(self, path, universe, pause=0):
        def main(path, universe, pause):
            name = os.path.basename(path)
            # log.debug(">> ... saving [%s] in %s secs ...", name, pause)                
            time.sleep(pause)
            try:
                os.makedirs(os.path.dirname(path), exist_ok=True)                
                yaml.dump(universe, open(path, "w", encoding="utf-8"), Dumper=yaml.Dumper)
            except Exception as why:
                log.error("%s: Error savig: %s: %s", self, path, why)
            # log.debug("<< ... saving [%s] in %s secs DONE", name, pause)                
                
        # uses a background thread to save in YAML format
        # because is too slow to block the main thread
        #th = threading.Thread(target=main)
        #th.start()
        p = Process(target=main, args=(path, universe, pause), daemon=True)
        self.background.append(p)
        p.start()
        #log.debug("saving daemon is running:  %s", p.is_alive())
        foo = 1
                    

# class SurrealStorage(StoragePort):
#     def __init__(self, url="./db", user="root", password="root", ns="test", db="test"):
#         # super().__init__(url) # TODO: FIXME: DO NOT CALL BASE CLASS, will corrupt url
#         self.url = url
#         self.cache = {}
#         self.user = user
#         self.password = password
#         self.ns = ns
#         self.db = db
#         self.connection = None

#     async def _connect(self):
#         self.connection = Surreal(self.url)

#         # TODO: use credentials
#         await self.connection.connect()
#         await self.connection.signin({"user": self.user, "pass": self.password})
#         await self.connection.use(self.ns, self.db)

#     async def get(self, fqid, cache=False):
#         if cache:
#             data = self.cache.get(fqid)
#         else:
#             data = None
#         if data is None:
#             if not self.connection:
#                 await self._connect()
#             try:
#                 data = await self.connection.select(fqid)
#             except Exception as why:
#                 log.warning(why)

#             if not cache:
#                 self.cache[fqid] = data

#         return data

#     async def put(self, fqui, data) -> bool:
#         if not self.connection:
#             await self._connect()
#         try:
#             thing = data.pop("id")
#             result = await self.connection.update(thing, data)
#         except Exception as why:
#             print(f"ERROR: {why}")

#         # t1 = time.time()
#         # print(f"{self.__class__}.set() : elapsed = {t1-t0} seconds")

#     async def set(self, fqid, data, merge=False):
#         t0 = time.time()
#         if merge:
#             data0 = self.get(table)
#             # data = {** data0, ** data} # TODO: is faster?
#             data0.update(data)
#             data = data0

#         if not self.connection:
#             await self._connect()

#         # await self.connection.query(f"USE DB {table.replace('.', '_')};")

#         for kind, items in data.items():
#             for id_, item in items.items():
#                 result = await self.connection.update(
#                     kind,
#                     item,
#                 )
#         t1 = time.time()
#         print(f"{self.__class__}.set() : elapsed = {t1-t0} seconds")


class SurrealistStorage(Storage):
    def __init__(self, url="./db", user="root", password="root", ns="test", db="test"):
        super().__init__(url) # TODO: FIXME: DO NOT CALL BASE CLASS, will corrupt url
        self.url = url
        self.cache = {}
        self.user = user
        self.password = password
        self.ns = ns
        self.db = db
        self.surreal = None
        self.connection = None

    async def _connect(self):
        url = parse_uri(self.url)
        url["fscheme"] = "http"
        url["path"] = ""
        url = build_uri(**url)

        self.surreal = Surrealist(
            url,
            namespace=self.ns,
            database=self.db,
            credentials=(self.user, self.password),
            use_http=False,
            timeout=10,
            log_level="ERROR",
        )
        print(self.surreal.is_ready())
        print(self.surreal.version())

        self.connection = self.surreal.connect()

        # TODO: use credentials
        # await self.connection.connect()
        # await self.connection.signin({"user": self.user, "pass": self.password})
        # await self.connection.use(self.ns, self.db)

    async def get(self, fqid, cache=True):
        if cache:
            data = self.cache.get(fqid)
        else:
            data = None
        if data is None:
            if not self.connection:
                await self._connect()
            try:
                res = self.connection.select(fqid)
                result = res.result
                if result:
                    data = result[0]
            except Exception as why:
                log.warning(why)

            if not cache:
                self.cache[fqid] = data

        return data

    async def put(self, fqid, data) -> bool:
        if not self.connection:
            await self._connect()
        try:
            thing = data.pop("id")
            assert thing == fqid
            result = self.connection.update(thing, data)
            return result.status in ("OK",)
        except Exception as why:
            print(f"ERROR: {why}")

    async def set(self, fqid, data, merge=False):
        t0 = time.time()
        table, uid = split_fqui(fqid)
        if merge:
            data0 = self.get(table)
            # data = {** data0, ** data} # TODO: is faster?
            data0.update(data)
            data = data0

        if not self.connection:
            await self._connect()

        # await self.connection.query(f"USE DB {table.replace('.', '_')};")
        # TODO: review this code
        for kind, items in data.items():
            for _, item in items.items():
                _ = self.connection.update(
                    kind,
                    item,
                )
        t1 = time.time()
        print(f"{self.__class__}.set() : elapsed = {t1-t0} seconds")

    async def save(self, nice=False):
        "TBD"
        return True

    async def info(self):
        "TBD"
        return {}


class DualStorage(PickleStorage):
    """Storage for debugging and see all data in yaml
    Low performance, but is just for testing
    """

    def __init__(self, url="./db", klass=YamlStorage):
        super().__init__(url)
        self.other = klass(url)
        self.background = self.other.background

    async def get(self, fqid, query=None, **params):
        other_mtime = None
        if not self.other.lock:
            table, uid = split_fqui(fqid)
            other_path = self.other._file(table)
            mine_path = self._file(table)
            try:
                other_mtime = os.stat(other_path).st_mtime
                mine_mtime = os.stat(mine_path).st_mtime
            except Exception:
                mine_mtime = 0
        else:
            foo = 1
                
        if other_mtime is not None:
            if other_mtime > mine_mtime:
                # replace table from newer to older one
                universe = self.other._load(table)
                super()._save(table, universe)
                self.cache[table] = universe
            data = await super().get(fqid, query=None, **params)
        else:
            data = {}
        return data

    async def set(self, fqid, data, merge=False):
        """
        other.mtime < mine.mtime
        otherwise user has modifier `yaml` file and `pickle` will be updated
        """
        res1 = await self.other.set(fqid, data, merge)
        res2 = await super().set(fqid, data, merge)
        return all([res1, res2])

    async def put(self, fqid, data):
        res1 = await super().put(fqid, data)
        res2 = await self.other.put(fqid, data)
        return all([res1, res2])

    def _save(self, table, universe=None, pause=0):
        self.other._save(table, universe, pause=pause)
        super()._save(table, universe, pause=pause)

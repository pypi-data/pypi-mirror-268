import atexit
import datetime
import enum
import pathlib
import sqlite3
from collections import namedtuple

from pubsub import pub

TABLE = "id INTEGER PRIMARY KEY, type_ TEXT NOT NULL, date_time datetime NOT NULL, message TEXT NOT NULL, detail TEXT, context TEXT"

sqlite3.register_adapter(datetime.datetime, lambda x: x.isoformat())
sqlite3.register_converter(
    "datetime", lambda x: datetime.datetime.fromisoformat(x.decode())
)


class Level(enum.Enum):
    TRACE = 5
    DEBUG = 10
    VERBOSE = 15
    INFO = 20
    SUCCESS = 25
    WARNING = 30
    ERROR = 40
    CRITICAL = 50


Row = namedtuple('Row', ('id', 'type', 'date_time', 'message', 'detail', 'context'))


class Table:
    def __new__(cls, path: pathlib.Path):
        it = cls.__dict__.get("__it__")
        if it is not None:
            return it
        cls.__it__ = it = object.__new__(cls)
        it.__init(path=path)
        return it

    def __init(self, path: pathlib.Path):
        self._database = sqlite3.connect(path, detect_types=sqlite3.PARSE_DECLTYPES)
        self._cursor = self._database.cursor()
        self._cursor.execute(f"CREATE TABLE IF NOT EXISTS applog ({TABLE})")
        self._timer = None

    def write(
        self,
        type_: str,
        message: str,
        detail: str = None,
        context: str = None,
    ):
        now = datetime.datetime.utcnow()
        self._cursor.execute(
            "INSERT INTO applog (type_, date_time, message, detail, context) VALUES(?, ?, ?, ?, ?)",
            (type_, now, message, detail, context),
        )
        self._database.commit()
        pub.sendMessage('netlink.applog.append', type_=type_, date_time=now, message=message, detail=detail, context=context)

    def read(self):
        self._cursor.execute("SELECT * FROM applog ORDER BY id DESC")
        return tuple([Row(*i) for i in self._cursor.fetchall()])

    @classmethod
    def close(cls):
        it = cls.__dict__.get("__it__")
        it._database.commit()
        it._cursor.close()
        it._database.close()


atexit.register(Table.close)


class ApplicationLog:

    def __init__(self, context: str = None, level: Level = Level.INFO):
        self._table = Table(pathlib.Path(__name__).parent / "applog.db")
        self._context = context
        self._level = level

    def log(self, level: int, message: str, detail: str = None):
        if level >= self._level.value:
            self._table.write(Level(level).name, message, detail, context=self._context)

    def trace(self, message: str, detail: str = None):
        self.log(Level.TRACE.value, message, detail)

    def debug(self, message: str, detail: str = None):
        self.log(Level.DEBUG.value, message, detail)

    def verbose(self, message: str, detail: str = None):
        self.log(Level.VERBOSE.value, message, detail)

    def info(self, message: str, detail: str = None):
        self.log(Level.INFO.value, message, detail)

    def success(self, message: str, detail: str = None):
        self.log(Level.SUCCESS.value, message, detail)

    def warning(self, message: str, detail: str = None):
        self.log(Level.WARNING.value, message, detail)

    def error(self, message: str, detail: str = None):
        self.log(Level.ERROR.value, message, detail)

    def critical(self, message: str, detail: str = None):
        self.log(Level.CRITICAL.value, message, detail)


logger = ApplicationLog()


def prune_application_log(date_time: datetime.datetime):
    table = Table(pathlib.Path(__name__).parent / "applog.db")
    stmt = f"DELETE FROM applog WHERE date_time <= '{date_time.isoformat()}'"
    table._cursor.execute(stmt)
    table.write("*** internal ***", "Pruned Application Log", stmt)
    table._database.commit()
    pub.sendMessage('netlink.applog.prune', limit=date_time)

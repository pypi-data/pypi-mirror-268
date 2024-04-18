import typing
import zoneinfo
from datetime import datetime
from tzlocal import get_localzone


def format_datetime(t: datetime,
                    fmt: str = '%Y-%m-%d %H:%M:%S%z',
                    tz: typing.Optional[str | zoneinfo.ZoneInfo] = None) -> str:

    tz = tz or get_localzone()
    return t.astimezone(tz).strftime(fmt)

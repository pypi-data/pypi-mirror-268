from __future__ import annotations

from datetime import datetime

from dateparser import parse as parse_datetime

from .api import SelectorOrElement
from .text import extract_text


def extract_datetime(
    node: SelectorOrElement | str,
    *,
    date_order: str | None = None,
    timezone: str | None = None,
    to_timezone: str | None = None,
    **kwargs,
) -> datetime | None:
    settings = kwargs.pop("settings", {})
    if date_order is not None:
        settings["DATE_ORDER"] = date_order
        settings.setdefault("PREFER_LOCALE_DATE_ORDER", False)
    if timezone is not None:
        settings["TIMEZONE"] = timezone
        settings.setdefault("RETURN_AS_TIMEZONE_AWARE", True)
    if to_timezone is not None:
        settings["TO_TIMEZONE"] = to_timezone
        settings.setdefault("RETURN_AS_TIMEZONE_AWARE", True)
    kwargs["settings"] = settings
    return parse_datetime(extract_text(node, guess_layout=False), **kwargs)

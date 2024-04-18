from __future__ import annotations

from typing import Any

from chompjs import parse_js_object, parse_js_objects

from .api import SelectorOrElement
from .text import extract_text


def extract_js_object(node: SelectorOrElement | str, **kwargs) -> dict[str, Any]:
    return parse_js_object(extract_text(node, guess_layout=False), **kwargs)


def extract_js_objects(node: SelectorOrElement | str, **kwargs) -> list[dict[str, Any]]:
    return list(parse_js_objects(extract_text(node, guess_layout=False), **kwargs))

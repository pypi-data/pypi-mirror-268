from __future__ import annotations

from typing import Any

import extruct

from .api import SelectorOrElement, input_to_element


def extract_structured_data(
    node: SelectorOrElement, **kwargs
) -> dict[str, list[dict[str, Any]]]:
    kwargs.setdefault("uniform", True)
    node = input_to_element(node)
    return extruct.extract(node, **kwargs)

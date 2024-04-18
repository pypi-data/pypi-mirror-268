from __future__ import annotations

import re

# FIXME use modified (br tag) extract_text
from zyte_parsers.utils import extract_text as _extract_text

from .api import SelectorOrElement


def extract_text(node: SelectorOrElement | str, guess_layout: bool = True) -> str:
    if isinstance(node, str):
        return node
    else:
        return _extract_text(node, guess_layout=guess_layout) or ""


def extract_term_definitions(
    node: SelectorOrElement | str,
    term: str,
    delimiter: str = ": ",
    *,
    multiline: bool = False,
    ignore_case: bool = False,
) -> list[str]:
    """
    >>> text = '''\\
    ... Size: Medium
    ... Color: Grass green
    ... Size: Large
    ... Color: Ocean blue'''
    >>> extract_term_definitions(text, 'Color')
    ['Grass green', 'Ocean blue']

    >>> text = '''
    ... Description
    ... Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
    ... incididunt ut labore et dolore magna aliqua.
    ...
    ... Features:
    ... - Nunc dignissim risus id metus.
    ... - Cras ornare tristique elit.
    '''
    >>> extract_term_definitions(text, 'Features', multiline=True)
    ['- Nunc dignissim risus id metus.\\n- Cras ornare tristique elit.']
    """
    pattern = compile_term_definition_re(
        term=term, delimiter=delimiter, multiline=multiline, ignore_case=ignore_case
    )
    return pattern.findall(extract_text(node))


def extract_text_fragments(
    node: SelectorOrElement | str,
    start: str = "",
    end: str = "",
    *,
    prefix: str = r"\A",
    suffix: str = r"\Z",
    ignore_case: bool = False,
) -> list[str]:
    pattern = compile_text_fragment_re(
        start=start, end=end, prefix=prefix, suffix=suffix, ignore_case=ignore_case
    )
    return pattern.findall(extract_text(node))


def compile_term_definition_re(
    term: str,
    delimiter: str = ": ",
    *,
    multiline: bool = False,
    ignore_case: bool = False,
) -> re.Pattern:
    if multiline:
        prefix = r"(?:\n\n|\A|\A\n)"
        suffix = r"(?:\n\n|\Z|\n\Z)"
    else:
        prefix = r"^"
        suffix = r"$"
    # `term` must be followed by a new line or `delimiter`
    prefix += rf"(?:{re.escape(term)})(?:\n|{re.escape(delimiter)})"
    return compile_text_fragment_re(
        prefix=prefix, suffix=suffix, ignore_case=ignore_case
    )


def compile_text_fragment_re(
    start: str = "",
    end: str = "",
    *,
    prefix: str = r"\A",
    suffix: str = r"\Z",
    ignore_case: bool = False,
) -> re.Pattern:
    pattern = rf"(?:{prefix})({start}.*?{end})(?:{suffix})"
    flags = re.MULTILINE | re.DOTALL
    if ignore_case:
        flags |= re.IGNORECASE
    return re.compile(pattern, flags)

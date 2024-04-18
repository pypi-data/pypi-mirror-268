import re
from urllib.parse import urlparse, urlunparse

from zyte_parsers.utils import extract_link as _extract_link

from .api import SelectorOrElement


def extract_url(node: SelectorOrElement, base_url: str = "") -> str | None:
    return _extract_link(node, base_url)


# based on
# https://github.com/scrapy/scrapely/blob/master/scrapely/extractors.py
# https://github.com/scrapinghub/portia2code/blob/master/portia2code/processors.py


# fmt: off
_IMAGE_FILE_EXTENSIONS = [
    'mng', 'pct', 'bmp', 'gif', 'jpg', 'jpeg', 'png', 'pst', 'psp',
    'tif', 'tiff', 'ai', 'drw', 'dxf', 'eps', 'ps', 'svg',
]
# fmt: on
_CSS_IMAGE_RE = re.compile(r"background(?:-image)?\s*:\s*url\((.*?)\)")
_GENERIC_PATH_RE = re.compile(r"/?(?:[^/]+/)*(?:.+)")
_IMAGE_PATH_RE = re.compile(
    rf'/?(?:[^/]+/)*(?:.+\.(?:{"|".join(_IMAGE_FILE_EXTENSIONS)}))'
)


def _strip_url(text):
    if text:
        return text.strip("\t\r\n '\"")


# TODO SelectorOrElement instead of text
def extract_image_url(text):
    text = _strip_url(text)
    img_url = None
    if text:
        # check if the text is style content
        match = _CSS_IMAGE_RE.search(text)
        text = match.groups()[0] if match else text
        parsed = urlparse(text)
        path = None
        match = _IMAGE_PATH_RE.search(parsed.path)
        if match:
            path = match.group()
        elif parsed.query:
            match = _GENERIC_PATH_RE.search(parsed.path)
            if match:
                path = match.group()
        if path is not None:
            parsed = list(parsed)
            parsed[2] = path
            img_url = urlunparse(parsed)
        if not img_url:
            img_url = text
    return img_url

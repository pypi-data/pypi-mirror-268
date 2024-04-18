# pyright: reportPrivateImportUsage=false
from clear_html import clean_node, cleaned_node_to_html

from .api import SelectorOrElement, input_to_element


def extract_clear_html(node: SelectorOrElement) -> str:
    node = input_to_element(node)
    return cleaned_node_to_html(clean_node(node))

from typing import Optional

from .types import Quality, CriteriaTreeElement, Criterion, TaskGroup, Task


def to_color_hex_string(color):
    if isinstance(color, str):
        return color
    return f"#{color.red:02x}{color.green:02x}{color.blue:02x}"


def should_hide_code(element: CriteriaTreeElement | str | dict) -> bool:
    if isinstance(element, str):
        return element.startswith('_')
    if isinstance(element, dict):
        code: Optional[str] = element.get('code', None)
        if code is None:
            raise ValueError("Element must have a 'code' key")
        return code.startswith('_')
    return element.code.startswith('_')


def get_qualified_name(element: Quality | Criterion | TaskGroup | Task | dict) -> str:
    if isinstance(element, dict):
        title, code = (element.get('title', None), element.get('code', None))
        if title is None or code is None:
            raise ValueError("Element must have 'title' and 'code' keys")
    else:
        title, code = element.title, element.code
    if code.startswith('_'):
        code = code[1:]
    if element.title == code:
        return element.title
    return f"{code} {element.title}"


def resolve_code(element: CriteriaTreeElement | str | dict) -> str:
    if isinstance(element, str):
        resolved_code = element
    elif isinstance(element, dict):
        resolved_code = element.get('code', None)
        if resolved_code is None:
            raise ValueError("Element must have a 'code' key")
    else:
        resolved_code = element.code
    return resolved_code[1:] if resolved_code.startswith('_') else resolved_code

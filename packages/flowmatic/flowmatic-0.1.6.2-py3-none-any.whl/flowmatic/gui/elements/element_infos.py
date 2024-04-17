from typing import Callable, NamedTuple


Element = NamedTuple


class Button(Element):
    text: str
    command: Callable[[], None]


class Info(Element):
    label: str
    value: str


class ElementFrame(Element):
    title: str
    rows: list[Element]

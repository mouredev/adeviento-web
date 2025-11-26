from enum import Enum

import reflex as rx

from .colors import Color, TextColor
from .fonts import Font

MAX_WIDTH = "1000px"
FLEX_DIRECTION = ["column", "column", "column", "row", "row"]


class SizeEM(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    BIG = "2em"
    BUTTON = "2.75em"
    VERY_BIG = "4em"


class Size(Enum):
    SMALL = "3"
    DEFAULT = "4"  # 1em
    MEDIUM = "5"
    BIG = "6"
    VERY_BIG = "9"  # 3em


STYLESHEETS = [
    "/css/main.css",
    "https://unpkg.com/nes.css@latest/css/nes.min.css",
    "https://fonts.googleapis.com/css?family=Press+Start+2P&display=swap",
]

BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "color": TextColor.PRIMARY.value,
    "background": Color.PRIMARY.value,
    rx.heading: {
        "font_family": Font.DEFAULT.value,
        "color": TextColor.ACCENT.value,
        "margin_bottom": SizeEM.ZERO.value,
    },
    rx.text: {"margin_bottom": SizeEM.ZERO.value},
    rx.link: {
        "text_decoration": "none",
        "_hover": {"color": TextColor.ACCENT.value, "text_decoration": "none"},
    },
    rx.el.span: {"font_size": SizeEM.MEDIUM.value},
    rx.button: {
        "margin_bottom": SizeEM.DEFAULT.value,
        "height": SizeEM.BUTTON.value,
        "color": f"{TextColor.SECONDARY.value} !important",
        "_hover": {"color": f"{TextColor.PRIMARY.value} !important"},
    },
}

max_width_style = dict(
    align_items="start", padding_x=SizeEM.BIG.value, width="100%", max_width=MAX_WIDTH
)

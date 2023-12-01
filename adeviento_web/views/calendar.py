import reflex as rx
import adeviento_web.constants as constants
import adeviento_web.styles.styles as styles
from adeviento_web.styles.styles import Size
from adeviento_web.styles.colors import TextColor
from adeviento_web.components.header_text import header_text
from adeviento_web.components.button import button
from adeviento_web.components.day import day


_gifts = [
    (
        "(x5) Git y GitHub desde cero: Guía de estudio teórico-práctica paso a paso más curso en vídeo",
        "https://x.com/MoureDev/status/1730591277752676796?s=20",
        "https://mouredev.link/libro-git"
    )
]

_current_day = len(_gifts)


def calendar() -> rx.Component:
    return rx.vstack(
        header_text(
            "heart",
            "Calendario"
        ),
        rx.vstack(
            rx.text(
                "El regalo del hoy",
                class_name="title",
                color=TextColor.ACCENT.value
            ),
            rx.flex(
                rx.box(
                    day(
                        _current_day,
                        _gift_name(_current_day),
                        _gift_url(_current_day),
                    ),
                    height="14em",
                    width="14em",
                    aspect_ratio="1",
                    margin_right=Size.BIG.value
                ),
                rx.vstack(
                    rx.span(
                        f"Día {_current_day}"),
                    rx.link(
                        _gift_name(_current_day),
                        href=_gift_info(_current_day),
                        is_external=True
                    ),
                    rx.spacer(),
                    button(
                        "Participa",
                        _gift_url(_current_day)
                    ),
                    align_items="start",
                    margin_top=Size.BIG.value
                ),
                direction=styles.FLEX_DIRECTION
            ),
            class_name="nes-container is-dark with-title",
            align_items="start"
        ),
        rx.responsive_grid(
            day(1, _gift_name(1), _gift_url(1)),
            rx.foreach(
                list(range(2, 25)),
                lambda number:
                day(
                    number
                )
            ),
            columns=[3, 3, 4, 5, 6],
            spacing=Size.DEFAULT.value,
            width="100%",
            padding_y=Size.BIG.value
        ),
        rx.vstack(
            rx.hstack(
                rx.text(
                    "Próximo regalo y ganadores en",
                    margin_right=Size.DEFAULT.value
                ),
                rx.text(
                    id="countdown",
                    margin_left=Size.ZERO.value
                ),
                align_items="start",
                flex_direction=styles.FLEX_DIRECTION
            ),
            # button(
            #     "Recordar",
            #     constants.DISCORD_EVENT_URL
            # ),
            rx.span(
                "• Los regalos son sorpresa, permanecerán ocultos hasta el día de su publicación. No olvides pasarte por aquí cada día para descubrir un nuevo sorteo."
            ),
            class_name="nes-container is-dark",
            align_items="start",
            width="100%"
        ),
        rx.script(src="/js/countdown.js"),
        style=styles.max_width_style
    )


def _gift_name(gift) -> str:
    gift_index = gift - 1
    if len(_gifts) > gift_index:
        return _gifts[gift_index][0]
    return ""


def _gift_url(gift) -> str:
    gift_index = gift - 1
    if len(_gifts) > gift_index:
        return _gifts[gift_index][1]
    return ""


def _gift_info(gift) -> str:
    gift_index = gift - 1
    if len(_gifts) > gift_index:
        return _gifts[gift_index][2]
    return ""

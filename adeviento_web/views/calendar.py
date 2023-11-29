import reflex as rx
import adeviento_web.constants as constants
import adeviento_web.styles.styles as styles
from adeviento_web.styles.styles import Size
from adeviento_web.components.header_text import header_text
from adeviento_web.components.button import button
from adeviento_web.components.day import day


def calendar() -> rx.Component:
    return rx.vstack(
        header_text(
            "heart",
            "Calendario"
        ),
        rx.vstack(
            rx.hstack(
                rx.text(
                    "El evento comienza en",
                    margin_right=Size.DEFAULT.value
                ),
                rx.text(
                    id="countdown",
                    margin_left=Size.ZERO.value
                ),
                align_items="start",
                flex_direction=styles.FLEX_DIRECTION
            ),
            button(
                "Recordar",
                constants.DISCORD_EVENT_URL
            ),
            rx.span(
                "• Los regalos son sorpresa, permanecerán ocultos hasta el día de su publicación. No olvides pasarte por aquí cada día para descubrir un nuevo sorteo."
            ),
            class_name="nes-container is-dark",
            align_items="start",
            width="100%"
        ),
        rx.responsive_grid(
            rx.foreach(
                list(range(1, 25)),
                lambda number:
                day(
                    number
                )
            ),
            columns=[3, 3, 4, 5, 6],
            spacing=Size.DEFAULT.value,
            width="100%",
            padding_top=Size.BIG.value
        ),
        rx.script(src="/js/countdown.js"),
        style=styles.max_width_style,
    )

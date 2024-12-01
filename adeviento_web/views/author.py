import reflex as rx
import datetime
import adeviento_web.constants as constants
import adeviento_web.styles.styles as styles
from adeviento_web.styles.styles import Size, Color, TextColor
from adeviento_web.components.header_text import header_text
from adeviento_web.components.button import button


def author() -> rx.Component:
    return rx.vstack(
        header_text(
            "like",
            "Hola, mi nombre es Brais Moure"
        ),
        rx.flex(
            rx.image(
                src="avatar.jpg",
                width="128px",
                height="128px",
                bg=Color.PRIMARY.value,
                padding="2px",
                border=f"4px solid {Color.SECONDARY.value}",
                border_radius="50%",
                margin_right=Size.SMALL.value,
                margin_bottom=Size.SMALL.value
            ),
            rx.vstack(
                rx.el.span(
                    f"Soy ingeniero de software desde hace más de {
                        _experience()} años."
                ),
                rx.el.span(
                    "En 2018 comencé a divulgar contenido sobre programación y desarrollo de software en redes sociales como ",
                    rx.el.span(
                        "@mouredev",
                        color=TextColor.ACCENT.value,
                        font_size=Size.DEFAULT.value
                    ),
                    "."
                ),
                _author_buttons(),
                width="100%",
                align_items="start"
            ),
            align_items="start",
            spacing=Size.BIG.value,
            flex_direction=styles.FLEX_DIRECTION
        ),
        style=styles.max_width_style
    )


def _author_buttons() -> rx.Component:
    return rx.flex(
        button(
            "YouTube",
            constants.YOUTUBE_URL
        ),
        button(
            "Twitch",
            constants.TWITCH_URL
        ),
        button(
            "Discord",
            constants.DISCORD_URL
        ),
        align_items="start",
        flex_direction=styles.FLEX_DIRECTION
    )


def _experience() -> int:
    return datetime.date.today().year - 2010

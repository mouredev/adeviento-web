import reflex as rx
import adeviento_web.styles.styles as styles
from adeviento_web.styles.styles import Size, Color
from adeviento_web.components.header_text import header_text


def partners() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            header_text(
                "star",
                "Patrocinado por",
                False
            ),
            rx.responsive_grid(
                _partner_link(
                    "elgato.png",
                    "https://e.lga.to/MoureDev"
                ),
                _partner_link(
                    "geekshubs.png",
                    "https://mouredev.com/geeks"
                ),
                _partner_link(
                    "raiola.png",
                    "https://mouredev.com/raiola"
                ),
                _partner_link(
                    "nuwe.png",
                    "https://nuwe.io"
                ),
                columns=[2, 2, 4, 4],
                spacing=Size.VERY_BIG.value
            ),
            padding_y=Size.VERY_BIG.value,
            style=styles.max_width_style
        ),
        bg=Color.ACCENT.value,
        width="100%"
    )


def _partner_link(image: str, url: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=image
        ),
        href=url,
        is_external=True
    )

import reflex as rx
import adeviento_web.styles.styles as styles
from adeviento_web.styles.styles import Size, Color
from adeviento_web.components.header_text import header_text


def partners() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            header_text(
                "star",
                "Con la ayuda de",
                False
            ),
            rx.responsive_grid(
                _partner_link(
                    "elgato.png",
                    "https://e.lga.to/MoureDev",
                    "Elgato"
                ),
                _partner_link(
                    "geekshubs.png",
                    "https://mouredev.com/geeks",
                    "GeeksHubs"
                ),
                _partner_link(
                    "raiola.png",
                    "https://mouredev.com/raiola",
                    "Raiola Networks"
                ),
                _partner_link(
                    "nuwe.png",
                    "https://nuwe.io",
                    "NUWE"
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


def _partner_link(image: str, url: str, alt: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=image,
            width="100%",
            height="100%",
            alt=alt
        ),
        href=url,
        is_external=True
    )

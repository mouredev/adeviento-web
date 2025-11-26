import reflex as rx

import adeviento_web.styles.styles as styles
from adeviento_web.components.header_text import header_text
from adeviento_web.styles.styles import Color, Size, SizeEM


def partners() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            header_text("star", "Con la ayuda de", False),
            rx.grid(
                _partner_link("elgato.png", "https://e.lga.to/MoureDev", "Elgato"),
                _partner_link("raiola.png", "https://mouredev.link/raiola", "Raiola Networks"),
                _partner_link("mouredevpro.png", "https://mouredev.pro", "mouredev pro"),
                columns=rx.breakpoints(initial="1", sm="3"),
                spacing=rx.breakpoints(
                    initial=Size.ZERO.value,
                    sm=Size.VERY_BIG.value,
                ),
            ),
            padding_y=SizeEM.VERY_BIG.value,
            style=styles.max_width_style,
        ),
        bg=Color.ACCENT.value,
        align="center",
        width="100%",
    )


def _partner_link(image: str, url: str, alt: str) -> rx.Component:
    return rx.link(
        rx.image(src=image, width="100%", height="100%", alt=alt), href=url, is_external=True
    )

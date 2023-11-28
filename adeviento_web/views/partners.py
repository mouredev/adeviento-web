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
            rx.text(
                "Con el apoyo de la comunidad y los patrocinadores costearé los 24 regalos. Imagínate tu logo aquí y en todas las comunicaciones diarias durante el evento."
            ),
            rx.span(
                "¿Quieres apoyar esta iniciativa? Escríbeme a braismoure@mouredev.com o envíame un mensaje en redes sociales ¡Gracias!"
            ),
            padding_y=Size.VERY_BIG.value,
            style=styles.max_width_style
        ),
        bg=Color.ACCENT.value,
        width="100%"
    )

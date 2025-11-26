import reflex as rx

import adeviento_web.constants as constants
import adeviento_web.styles.styles as styles
from adeviento_web.components.button import button
from adeviento_web.styles.styles import SizeEM, TextColor


def instructions() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text(
                "¿Cómo funciona el evento?",
                class_name="title",
                color=TextColor.ACCENT.value,
            ),
            rx.el.span(
                "• Del 1 al 24 de diciembre descubriré cada día un nuevo regalo en el calendario.",
                padding_top=SizeEM.DEFAULT.value,
            ),
            rx.el.span("• Puedes participar desde cualquier parte del mundo."),
            rx.el.span(
                "• Sólo tendrás que hacer Retweet a la publicación que enlazaré desde esta web. Tu cuenta de X/Twitter tiene que ser pública."
            ),
            button("X/Twitter", constants.TWITTER_URL),
            rx.el.span(
                "• Al día siguiente realizaré el sorteo de forma pública y compartiré el ganador en la web y en X/Twitter."
            ),
            rx.el.span(
                "• ¡Vuelta a empezar! Publicaré un nuevo regalo y comenzará de nuevo el proceso."
            ),
            class_name="nes-container is-dark with-title",
            align_items="start",
            width="100%",
        ),
        style=styles.max_width_style,
    )

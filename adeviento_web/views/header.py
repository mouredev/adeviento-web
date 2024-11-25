import reflex as rx
import adeviento_web.constants as constants
import adeviento_web.styles.styles as styles
from adeviento_web.styles.styles import Size, TextColor
from adeviento_web.components.button import button


def header() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Calendario de aDEViento 2024",
            size="lg",
            padding_bottom=Size.DEFAULT.value
        ),
        rx.flex(
            rx.image(
                src="mouredev.png",
                alt="Imagen pixel art de MoureDev con estilo navideño.",
                width="16em",
                height="16em",
                margin_right=Size.BIG.value
            ),
            rx.vstack(
                rx.box(
                    rx.text("24 días. 24 regalos."),
                    rx.text("Del 1 al 24 de diciembre."),
                    class_name="nes-balloon from-left is-dark"
                ),
                rx.el.span(
                    "Por cuarto año, ¡aquí está el calendario de adviento sorpresa de nuestra ",
                    rx.el.span(
                        "comunidad de developers",
                        color=TextColor.ACCENT.value,
                        font_size=Size.DEFAULT.value
                    ),
                    "!"
                ),
                rx.el.span(
                    "Una actividad en la que cada día sortearé un regalo relacionado con programación y desarrollo de software (libros, cursos…)."
                ),
                rx.el.span(
                    "Su finalidad es ayudar a compartir conocimiento y fomentar el aprendizaje en comunidad."
                ),
                button(
                    "Discord",
                    constants.DISCORD_URL
                ),
                rx.link(
                    "#aDEViento2024",
                    href=constants.ADEVIENTO_HASHTAG_URL,
                    is_external=True,
                    color=TextColor.TERTIARY.value
                ),
                align_items="start"
            ),
            flex_direction=styles.FLEX_DIRECTION
        ),
        padding_top=Size.VERY_BIG.value,
        style=styles.max_width_style
    )

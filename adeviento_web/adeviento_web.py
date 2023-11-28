import reflex as rx
import adeviento_web.styles.styles as styles
from adeviento_web.styles.styles import Size
from adeviento_web.views.navbar import navbar
from adeviento_web.views.header import header
from adeviento_web.views.instructions import instructions
from adeviento_web.views.calendar import calendar
from adeviento_web.views.partners import partners
from adeviento_web.views.author import author
from adeviento_web.views.footer import footer
from adeviento_web.components.github import github


def index() -> rx.Component:
    return rx.box(
        rx.script("document.documentElement.lang='es'"),
        rx.script(src="/js/snow.js"),
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                instructions(),
                calendar(),
                author(),
                partners(),
                footer(),
                github(),
                width="100%",
                spacing=Size.VERY_BIG.value
            )
        )
    )


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)

app.add_page(
    index,
    title="Calendario de aDEViento 2023 | 24 días. 24 regalos.",
    description="Por tercer año, ¡aquí está el calendario de adviento sorpresa de nuestra comunidad de developers! Del 1 al 24 de diciembre."
)

app.compile()

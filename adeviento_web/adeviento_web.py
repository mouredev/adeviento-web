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

title = "Calendario de aDEViento 2024 | 24 días. 24 regalos."
description = "Por cuarto año, ¡aquí está el calendario de adviento sorpresa de nuestra comunidad de developers! Del 1 al 24 de diciembre."
preview = "https://adviento.dev/preview.jpg"


def index() -> rx.Component:
    return rx.box(
        rx.script("document.documentElement.lang='es'"),
        rx.script(src="/js/snow.js"),
        navbar(),
        rx.vstack(
            header(),
            calendar(),
            partners(),
            instructions(),
            author(),
            footer(),
            github(),
            align="center",
            width="100%",
            spacing=Size.VERY_BIG.value
        )
    )


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
    head_components=[
        rx.script(src="https://www.googletagmanager.com/gtag/js?id=G-Y6GDVB3FJB"),
        rx.script(
            """
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'G-Y6GDVB3FJB');
"""
        ),
    ],
)


app.add_page(
    index,
    title=title,
    description=description,
    image=preview,
    meta=[
        {"name": "og:type", "content": "website"},
        {"name": "og:title", "content": title},
        {"name": "og:description", "content": description},
        {"name": "og:image", "content": preview},
        {"name": "twitter:card", "content": "summary_large_image"},
        {"name": "twitter:site", "content": "@mouredev"}
    ]
)

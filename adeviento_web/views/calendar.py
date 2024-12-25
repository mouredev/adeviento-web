import reflex as rx
import adeviento_web.constants as constants
import adeviento_web.styles.styles as styles
from adeviento_web.styles.styles import Size
from adeviento_web.styles.colors import TextColor
from adeviento_web.components.header_text import header_text
from adeviento_web.components.button import button
from adeviento_web.components.day import day


_gifts = [
    (
        "Git y GitHub desde cero: Guía de estudio teórico-práctica paso a paso más curso en vídeo",
        "https://x.com/MoureDev/status/1863584564389498883",
        "https://mouredev.link/libro-git"
    ),
    (
        "Suscripción mensual a mouredev pro: Estudia programación de manera diferente",
        "https://x.com/MoureDev/status/1863948284823224616",
        "https://mouredev.pro"
    ),
    (
        "Entiende la tecnología: Desde la caída de Megaupload hasta los secretos de la IA",
        "https://x.com/MoureDev/status/1864305488852115509",
        "https://amzn.to/41g9Fsx"
    ),
    (
        "Dominando JavaScript: Técnicas avanzadas para el desarrollo web moderno",
        "https://x.com/MoureDev/status/1864671641638252558",
        "https://amzn.to/4glh3av"
    ),
    (
        "Código Sostenible: Cómo programar código fácil de mantener",
        "https://x.com/MoureDev/status/1865031348630569137",
        "https://savvily.es/libros/codigo-sostenible"
    ),
    (
        "Suscripción mensual a Commit Academy",
        "https://x.com/MoureDev/status/1865405635010953329",
        "https://www.commitacademy.io"
    ),
    (
        "Ultimate Python: de cero a experto",
        "https://x.com/MoureDev/status/1865764060899528831",
        "https://amzn.to/4f1Hd0Q"
    ),
    (
        "Aprender a programar con C#",
        "https://x.com/MoureDev/status/1866118735733391715",
        "https://amzn.to/3D5m4FK"
    ),
    (
        "Git y GitHub desde cero: Guía de estudio teórico-práctica paso a paso más curso en vídeo",
        "https://x.com/MoureDev/status/1866474265555464506",
        "https://mouredev.link/libro-git"
    ),
    (
        "Suscripción mensual a mouredev pro: Estudia programación de manera diferente",
        "https://x.com/MoureDev/status/1866846649496056029",
        "https://mouredev.pro"
    ),
    (
        "Curso Jetpack Compose o Firebase AppCademy",
        "https://x.com/MoureDev/status/1867211119858741427",
        "https://www.appcademy.dev"
    ),
    (
        "Suscripción mensual a Hack4u: Aprende ciberseguridad",
        "https://x.com/MoureDev/status/1867571444101919104",
        "https://hack4u.io"
    ),
    (
        "El programador pragmático: Viaje a la maestría",
        "https://x.com/MoureDev/status/1867953183001088098",
        "https://amzn.to/4g9awQx"
    ),
    (
        "Suscripción mensual a Metal Code: Cursos enfocados al aprendizaje por conceptos",
        "https://x.com/MoureDev/status/1868286906120991048",
        "https://courses.metalcode.io"
    ),
    (
        "Suscripción mensual a Hola Mundo: Cursos de programación para todo el mundo",
        "https://x.com/MoureDev/status/1868664418483273859",
        "https://academia.holamundo.io"
    ),
    (
        "Git y GitHub desde cero: Guía de estudio teórico-práctica paso a paso más curso en vídeo",
        "https://x.com/MoureDev/status/1869019301396779037",
        "https://mouredev.link/libro-git"
    ),
    (
        "Suscripción mensual a mouredev pro: Estudia programación de manera diferente",
        "https://x.com/MoureDev/status/1869421281998946500",
        "https://mouredev.pro"
    ),
    (
        "No todo es programar: 10 habilidades que todo programador necesita",
        "https://x.com/MoureDev/status/1869749468855484767",
        "https://amzn.to/3ZMCDPw"
    ),
    (
        "Clean JavaScript: Código Limpio, SOLID y testing",
        "https://x.com/MoureDev/status/1870103870837264610",
        "https://cleanjavascript.es"
    ),
    (
        "Patrones de diseño",
        "https://x.com/MoureDev/status/1870471993562476946",
        "https://refactoring.guru/es/design-patterns/book"
    ),
    (
        "Curso intensivo de Python",
        "https://x.com/MoureDev/status/1870849647360766330",
        "https://amzn.to/4gnfg4Y"
    ),
    (
        "Dominio .dev (o .com) anual en Raiola Networks",
        "https://x.com/MoureDev/status/1871213692160721380",
        "https://mouredev.link/raiola"
    ),
    (
        "Git y GitHub desde cero: Guía de estudio teórico-práctica paso a paso más curso en vídeo",
        "https://x.com/MoureDev/status/1871557969256783996",
        "https://mouredev.link/libro-git"
    ),
    (
        "Suscripción anual a mouredev pro: Estudia programación de manera diferente",
        "https://x.com/MoureDev/status/1871934793124061382",
        "https://mouredev.pro"
    )
]

_current_day = len(_gifts) - 1


def calendar() -> rx.Component:
    return rx.vstack(
        header_text(
            "heart",
            "Calendario 2024.¡Feliz Navidad!"
        ),
        # rx.vstack(
        #     rx.text(
        #         "El regalo de hoy",
        #         class_name="title",
        #         color=TextColor.ACCENT.value
        #     ),
        #     rx.flex(
        #         rx.box(
        #             day(
        #                 _current_day + 1,
        #                 _gift_name(_current_day),
        #                 _gift_url(_current_day),
        #             ),
        #             height="14em",
        #             width="14em",
        #             aspect_ratio="1",
        #             margin_right=Size.BIG.value
        #         ),
        #         rx.vstack(
        #             rx.el.span(
        #                 f"Día {_current_day + 1}"),
        #             rx.link(
        #                 _gift_name(_current_day),
        #                 href=_gift_info(_current_day),
        #                 is_external=True
        #             ),
        #             rx.spacer(),
        #             rx.flex(
        #                 button(
        #                     "Participa",
        #                     _gift_url(_current_day)
        #                 ),
        #                 rx.cond(
        #                     _current_day > 1,
        #                     button(
        #                         f"Día {_current_day}",
        #                         _gift_url(_current_day - 1)
        #                     )
        #                 ),
        #                 align_items="start",
        #                 flex_direction=styles.FLEX_DIRECTION
        #             ),
        #             align_items="start",
        #             margin_top=Size.BIG.value
        #         ),
        #         flex_direction=styles.FLEX_DIRECTION
        #     ),
        #     width="100%",
        #     class_name="nes-container is-dark with-title",
        #     align_items="start"
        # ),
        rx.grid(
            *[
                day(
                    number + 1,
                    _gift_name(number),
                    _gift_url(number),
                    # False if len(_gifts) - 1 == number else True
                    True,  # finalizado
                )
                for _, number in enumerate(range(0, _current_day + 1))
            ],
            *[
                day(number)
                for _, number in enumerate(range(_current_day + 2, 25))
            ],
            columns=rx.breakpoints(
                initial="2",
                xs="3",
                sm="4",
                md="5",
                lg="6",
                xl="6"
            ),
            spacing=Size.DEFAULT.value,
            width="100%",
            padding_y=Size.BIG.value
        ),
        # rx.vstack(
        #     rx.hstack(
        #         rx.text(
        #             "Próximo regalo y ganadores en",
        #             # "Calendario 2024 en",
        #             margin_right=Size.DEFAULT.value
        #         ),
        #         rx.text(
        #             id="countdown",
        #             margin_left=Size.ZERO.value
        #         ),
        #         align_items="start",
        #         flex_direction=styles.FLEX_DIRECTION
        #     ),
        #     # button(
        #     #     "Recordar",
        #     #     constants.DISCORD_EVENT_URL
        #     # ),
        #     rx.el.span(
        #         "• Los regalos son sorpresa, permanecerán ocultos hasta el día de su publicación. No olvides pasarte por aquí cada día para descubrir un nuevo sorteo."
        #     ),
        #     rx.el.span(
        #         "• Puedes seleccionar cada regalo para conocer a los ganadores una vez se haya publicado el nuevo sorteo (aparecerá en rojo)."
        #     ),
        #     class_name="nes-container is-dark",
        #     align_items="start",
        #     width="100%"
        # ),
        # rx.script(src="/js/countdown.js"),
        style=styles.max_width_style
    )


def _gift_name(gift) -> str:
    gift_index = gift
    if len(_gifts) > gift_index:
        return _gifts[gift_index][0]
    return ""


def _gift_url(gift) -> str:
    gift_index = gift
    if len(_gifts) > gift_index:
        return _gifts[gift_index][1]
    return ""


def _gift_info(gift) -> str:
    gift_index = gift
    if len(_gifts) > gift_index:
        return _gifts[gift_index][2]
    return ""

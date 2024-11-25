import reflex as rx
import adeviento_web.constants as constants
import adeviento_web.styles.styles as styles
from adeviento_web.styles.styles import Size
from adeviento_web.styles.colors import TextColor
from adeviento_web.components.header_text import header_text
from adeviento_web.components.button import button
from adeviento_web.components.day import day


_gifts = []

_current_day = len(_gifts) - 1


def calendar() -> rx.Component:
    return rx.vstack(
        header_text(
            "heart",
            "Calendario 2024"
        ),
        rx.vstack(
            rx.hstack(
                rx.text(
                    # "Próximo regalo y ganadores en",
                    "Calendario 2024 en",
                    margin_right=Size.DEFAULT.value
                ),
                rx.text(
                    id="countdown",
                    margin_left=Size.ZERO.value
                ),
                align_items="start",
                flex_direction=styles.FLEX_DIRECTION
            ),
            # button(
            #     "Recordar",
            #     constants.DISCORD_EVENT_URL
            # ),
            rx.span(
                "• Los regalos son sorpresa, permanecerán ocultos hasta el día de su publicación. No olvides pasarte por aquí cada día para descubrir un nuevo sorteo."
            ),
            rx.span(
                "• Puedes seleccionar cada regalo para conocer a los ganadores una vez se haya publicado el nuevo sorteo (aparecerá en rojo)."
            ),
            class_name="nes-container is-dark",
            align_items="start",
            width="100%"
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
        #             rx.span(
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
        #                 button(
        #                     f"Día {_current_day}",
        #                     _gift_url(_current_day - 1)
        #                 ),
        #                 align_items="start",
        #                 direction=styles.FLEX_DIRECTION
        #             ),
        #             align_items="start",
        #             margin_top=Size.BIG.value
        #         ),
        #         direction=styles.FLEX_DIRECTION
        #     ),
        #     width="100%",
        #     class_name="nes-container is-dark with-title",
        #     align_items="start"
        # ),
        rx.responsive_grid(
            *[
                day(
                    number + 1,
                    _gift_name(number),
                    _gift_url(number),
                    True,  # finalizado
                    # False if len(_gifts) - 1 == number else True),
                )
                for _, number in enumerate(range(0, _current_day + 1))
            ],
            *[
                day(number)
                for _, number in enumerate(range(_current_day + 2, 25))
            ],
            columns=[3, 3, 4, 5, 6],
            spacing=Size.DEFAULT.value,
            width="100%",
            padding_y=Size.BIG.value
        ),
        rx.script(src="/js/countdown.js"),
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

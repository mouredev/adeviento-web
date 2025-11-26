import reflex as rx

from adeviento_web.styles.styles import Color, SizeEM


def day(number: int, text: str = "", url: str = "", finished=False) -> rx.Component:
    return rx.box(
        rx.cond(
            url != "",
            rx.link(
                rx.image(src=f"calendar/{number}.png", alt=text, padding=SizeEM.SMALL.value),
                href=url,
                is_external=True,
                position="absolute",
            ),
        ),
        rx.cond(
            url == "",
            rx.image(
                src="gift.png",
                alt=f"Regalo asociado al día {number}",
                position="absolute",
                padding=SizeEM.SMALL.value,
            ),
        ),
        rx.text(number, padding=SizeEM.DEFAULT.value, position="absolute"),
        bg=(
            Color.ACCENT.value
            if finished
            else Color.TERTIARY.value if url != "" else Color.SECONDARY.value
        ),
        aspect_ratio="1",
        position="relative",
    )

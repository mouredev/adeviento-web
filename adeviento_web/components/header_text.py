import reflex as rx

from adeviento_web.styles.styles import Size, SizeEM, TextColor


def header_text(icon: str, text: str, dark=True) -> rx.Component:
    return rx.hstack(
        rx.box(class_name=f"nes-icon is-medium {icon}"),
        rx.heading(
            text, size="6", color=TextColor.ACCENT.value if dark else TextColor.SECONDARY.value
        ),
        spacing=Size.DEFAULT.value,
        padding_bottom=SizeEM.BUTTON.value,
        align="center",
    )

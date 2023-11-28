import reflex as rx


def button(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            text,
            class_name="nes-btn is-error"
        ),
        href=url,
        is_external=True
    )

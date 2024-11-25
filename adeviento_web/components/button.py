import reflex as rx


def button(text: str, url: str) -> rx.Component:
    return rx.el.button(
        text,
        class_name="nes-btn is-error",
        on_click=rx.redirect(
            url,
            external=True
        )
    )

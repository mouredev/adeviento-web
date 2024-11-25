import reflex as rx


def link_icon(icon: str, url: str) -> rx.Component:
    return rx.el.i(
        "",
        class_name=f"nes-icon {icon} is-medium",
        on_click=rx.redirect(
            url,
            external=True
        )
    )

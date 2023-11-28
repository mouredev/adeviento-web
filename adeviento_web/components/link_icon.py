import reflex as rx


def link_icon(icon: str, url: str) -> rx.Component:
    return rx.link(
        "",
        class_name=f"nes-icon {icon} is-medium",
        href=url,
        is_external=True
    )

import reflex as rx
import adeviento_web.constants as constants
from adeviento_web.styles.styles import Size, Color
from adeviento_web.components.link_icon import link_icon


def navbar() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.image(
                src="mouredev.png",
                alt="Imagen pixel art de MoureDev con estilo navideño.",
                width="3em",
                height="3em"
            ),
            rx.text("aDEViento 2024"),
            rx.spacer(),
            rx.tablet_and_desktop(
                link_icon(
                    "youtube",
                    constants.YOUTUBE_URL
                )
            ),
            link_icon(
                "twitch",
                constants.TWITCH_URL
            ),
            link_icon(
                "github",
                constants.GITHUB_URL
            ),
            align="center",
            width="100%"
        ),
        bg=Color.PRIMARY.value,
        position="sticky",
        border_bottom=f"0.25em solid {Color.SECONDARY.value}",
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0",
        width="100%"
    )

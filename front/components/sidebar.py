import reflex as rx
from front.states.state_user import StateUser

def sidebar_item(
    text: str, icon: str
) -> rx.Component:
    return rx.button(
        rx.hstack(
            rx.icon(icon),
            rx.text(text, size="4", color=rx.color("accent", 11)),
            width="100%",
            padding_x="0.5rem",
            padding_y="0.75rem",
            align="center",
            style={
                "_hover": {
                    #"bg": rx.color("accent", 4),
                    "color": rx.color("accent", 4),
                },
                "background": "none",
                "border": "none",
                "border-radius": "0",
            },
        ),
        on_click= lambda: StateUser.set_component(text),
        underline="none",
        weight="medium",
        width="100%",
        background="none",
        border="none",
    )


def sidebar_items() -> rx.Component:
    return rx.vstack(
        sidebar_item("Create user", "layout-dashboard"),
        sidebar_item("Load users", "square-library"),
        sidebar_item("Update user", "bar-chart-4"),
        spacing="5",
        width="100%",
    )


def sidebar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.vstack(
                rx.box(height="20px"),
                sidebar_items(),
                spacing="5",
                #position="relative",
                #z_index="20",
                padding_x="1em",
                padding_y="1.5em",
                #padding="0",
                bg=rx.color("accent", 3),
                align="start",
                height="100vh", # el sidebar se extienda verticalmente
                width="16em",
                margin="0",
                displey="flex",
            ),
        ),
        rx.mobile_and_tablet(
            rx.drawer.root(
                rx.drawer.trigger(
                    rx.icon("align-justify", size=30)
                ),
                rx.drawer.overlay(z_index="5"),
                rx.drawer.portal(
                    rx.drawer.content(
                        rx.vstack(
                            rx.box(
                                rx.drawer.close(
                                    rx.icon("x", size=30)
                                ),
                                width="100%",
                            ),
                            sidebar_items(),
                            spacing="5",
                            width="100%",
                        ),
                        top="auto",
                        right="auto",
                        height="100%",
                        width="20em",
                        padding="1.5em",
                        bg=rx.color("accent", 2),
                    ),
                    width="100%",
                ),
                direction="left",
            ),
            padding="1em",
        ),
    )
import reflex as rx

def component_a() -> rx.Component:
    return rx.box(
        rx.text("Componente A", size="10", color=rx.color("blue", 11)),
        align="center",
        justify="center",
        height="100%",
        width="100%",
    )

def component_b() -> rx.Component:
    return rx.box(
        rx.text("Componente B", size="10", color=rx.color("red", 11)),
        align="center",
        justify="center",
        height="100%",
        width="100%",
    )

def component_c() -> rx.Component:
    return rx.box(
        rx.text("Componente C", size="10", color=rx.color("green", 11)),
        align="center",
        justify="center",
        height="100%",
        width="100%",
    )
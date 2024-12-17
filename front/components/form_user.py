import reflex as rx
from front.states.create_user import BackendState

def form_field(
    label: str, placeholder: str, type: str, name: str, on_change
) -> rx.Component:
    return rx.form.field(
        rx.flex(
            rx.form.label(label),
            rx.form.control(
                rx.input(
                    placeholder=placeholder,
                    type=type,
                    required=True,
                    style={
                        "height": "2.5rem",    # Ajusta la altura del input
                        "width": "100%",       # Asegura que el input ocupe todo el ancho disponible
                    },
                    on_change=on_change,
                ),
                as_child=True,
            ),
            direction="column",
            spacing="1",
        ),
        name=name,
        width="100%",
    )


def formUser() -> rx.Component:
    return rx.card(
        rx.flex(
            rx.hstack(
                rx.badge(
                    rx.icon(tag="user-plus", size=32),
                    color_scheme="blue",
                    radius="full",
                    padding="0.65rem",
                ),
                rx.vstack(
                    rx.heading(
                        "Create user",
                        size="4",
                        weight="bold",
                    ),
                    rx.text(
                        "Llena todos los campos",
                        size="2",
                    ),
                    spacing="1",
                    height="100%",
                ),
                height="100%",
                spacing="4",
                align_items="center",
                width="100%",
            ),
            rx.form.root(
                rx.flex(
                    rx.flex(
                        form_field(
                            "Name",
                            "Name",
                            "text",
                            "name",
                            BackendState.set_name
                        ),
                        form_field(
                            "Email",
                            "user@gmail.com",
                            "email",
                            "email",
                            BackendState.set_email
                        ),
                        spacing="3",
                        flex_direction=[
                            "column",
                            "row",
                            "row",
                        ],
                    ),
                    rx.flex(
                        form_field(
                            "Phone",
                            "Phone",
                            "tel",
                            "phone",
                            BackendState.set_phone
                        ),
                        form_field(
                            "Department",
                            "Department",
                            "text",
                            "department",
                            BackendState.set_department
                        ),
                        spacing="3",
                        flex_direction=[
                            "column",
                            "row",
                            "row",
                        ],
                    ),
                    rx.flex(
                        form_field(
                            "CC",
                            "CC",
                            "text",
                            "cc",
                            BackendState.set_cc
                        ),
                        spacing="3",
                        flex_direction=[
                            "column",
                            "row",
                            "row",
                        ],
                    ),
                    rx.flex(
                        rx.form.field(
                                rx.checkbox(
                                    "Active",
                                    default_checked=True,
                                    spacing="2",
                                    name="active",
                                    on_change=BackendState.set_active,
                                    ),
                        as_child=True,
                        direction="column",
                        spacing="1",
                        ),
                    ),
                    rx.flex(
                        rx.form.submit(
                            rx.button(
                                "Submit",
                                width="40%",
                                #on_click=BackendState.create_user,  
                            ),
                            as_child=True,
                        ),
                        justify="center",  # Centra el botón horizontalmente
                        align="center",    # Centra el botón verticalmente
                        width="100%",
                    ),
                    direction="column",
                    spacing="2",
                    width="100%",
                ),
                on_submit=BackendState.create_user,
                reset_on_submit=True,
            ),
            rx.text(
                BackendState.submission_status,
                color=rx.cond(
                    BackendState.submission_status.contains("success"),
                    "green",
                    "red"
                ),
                ),
            width="100%",
            direction="column",
            spacing="4",
        ),
        width="40%",
        height="80vh",
        padding="2em",
        box_shadow="lg",
        border_radius="lg",
    )
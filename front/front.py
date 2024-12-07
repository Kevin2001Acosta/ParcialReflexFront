import reflex as rx
from front.components.sidebar import sidebar
from front.components.nav_bar import navbar
from front.states.state_user import StateUser



app = rx.App()

def main_content() -> rx.Component:
    return rx.box(
        rx.text("holaaaaaaaaaaaaaaaa", size="10", color=rx.color("accent", 11)),
        align="center",
        justify="center",
        height="100%",
        width="100%",
        )


def index() -> rx.Component:
    return rx.box(
        rx.vstack(
            navbar(),
            rx.hstack(
                sidebar(),
                rx.box(
                    main_content(),
                    justify="center",
                    align="center",
                    padding="1rem",
                    height="100vh",
                    width="100%",
                    ),
                height="100vh",
                width="100%",
            ),
            width="100%",
        ),
        height="100vh",  
        bg=rx.color("gray",8,True),  
    )

app.add_page(index, route="/")



# ejecuta la aplicación

if __name__ == "__main__":
    app.run()

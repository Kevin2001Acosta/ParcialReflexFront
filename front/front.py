import reflex as rx
from front.components.sidebar import sidebar
from front.components.nav_bar import navbar
from front.states.state_user import StateUser



app = rx.App()

def main_content() -> rx.Component:
    return rx.box(
        rx.text("eeeeeeeeeeeee", size="10", color=rx.color("accent", 11)),
        display="flex",
        alignItems="center",
        justifyContent="center",
        height="100vh",
        width="100%",
        bg=rx.color("green",8,True),  
        #margin_left="16em",
        #margin_top="4em",
        #position="relative",
        )


def index() -> rx.Component:
    return rx.box(
        rx.vstack(
            navbar(),
            rx.hstack(
                sidebar(),
                main_content(),
                height="100%",
                width="100%",
                spacing="0",
            ),
            width="100%",
            spacing="0",
        ),
        height="100%",  
        bg=rx.color("gray",8,True),  
    )

app.add_page(index, route="/")



# ejecuta la aplicación

if __name__ == "__main__":
    app.run()

import reflex as rx
from front.components.sidebar import sidebar
from front.components.nav_bar import navbar
from front.states.state_user import StateUser
from front.components.components_example import component_b, component_c
from front.components.form_user import formUser
from tortoise.contrib.fastapi import register_tortoise
from backend.routes import user_routes
from front.components.table_users import tableUser




app = rx.App()

def main_content() -> rx.Component:
    return rx.cond(
        StateUser.get_component == "Create user",
        rx.box(
            formUser(),
            display="flex",
            alignItems="center",
            justifyContent="center",
            height="100vh",
            width="100%", 
        ),
        rx.cond(
            StateUser.get_component == "Load users",
            tableUser(),
            rx.cond(
                StateUser.get_component == "Update user",
                component_b(),
                rx.box(
                        rx.text("Bienvenido", size="50", color=rx.color("accent", 11)),
                        display="flex",
                        alignItems="center",
                        justifyContent="center",
                        height="100vh",
                        width="100%", 
                    )
            )
        )
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


async def read_root():
    return {"Hello": "World"}

app.api.add_api_route("/", read_root, methods=["Get"])  # define la ruta de la API
app.api.include_router(user_routes.router)

register_tortoise(
    app.api,
    db_url="postgres://postgres:Acos306254@localhost:5433/reflex",
    modules={"models": ["backend.models.user_model"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

# ejecuta la aplicación

if __name__ == "__main__":
    app.run()

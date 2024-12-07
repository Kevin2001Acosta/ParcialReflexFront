import reflex as rx

class StateUser(rx.State):
    """Define empty state to allow access to rx.State.router."""
    current_component: str = "hola"
    
    @rx.event
    def set_component(self, component_name: str):
        self.current_component = component_name
    
    @rx.var
    def get_component(self) -> str:
        return self.current_component
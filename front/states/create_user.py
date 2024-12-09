import reflex as rx
import requests as rq
class BackendState(rx.State):
    submission_status: str = ""
    loader: bool = False
    error: bool = False
    name: str = ""
    email: str = ""
    department: str = ""
    cc: str = ""
    phone: str = ""
    active: str = ""
    response: dict = {}



    @rx.event(background=True)
    async def create_user(self, data: dict):
        async with self:
            self.loader = True
            self.error = False
            print(data)
            response = rq.post("http://127.0.0.1:8000/users",json=data, headers={"Content-Type": "application/json"})
            print(1)
            if response.status_code == 200:
                self.submission_status = "user created success"
                self.response = response.json()
                print("Respuesta:",self.response)
                self.loader = False
            else:
                self.loader = False
                self.error = True
                self.submission_status = "User creation failed"

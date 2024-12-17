import reflex as rx
import requests as rq
from dotenv import load_dotenv
import os
from typing import List
from typing import Union

load_dotenv()

BACKEND_URL = os.getenv("BACKEND_URL")


class TableForEachState(rx.State):
    people: List[List[Union[int, str, bool]]] = []
    loader: bool = False
    submission_status: str = ""
    
    @rx.var
    def get_people(self) -> List[List[Union[int, str, bool]]]:
        return self.people
    
    
    @rx.event(background=True)
    async def fetch_people(self):
        async with self:
            self.loader = True
            response = rq.get(f"{BACKEND_URL}/users", headers={"Content-Type": "application/json"})
            if response.status_code == 200:
                self.submission_status = "Fetched users successfully"
                data: list = response.json()
                #print(data)
                self.people = [[person["id"], person["name"], person["email"], person["phone"], person["department"], person["cc"], person["active"]] for person in data]
                #print("Respuesta:",self.people)
                self.loader = False
            else:
                self.loader = False
                self.submission_status = "failed to fetch users"
    
    @rx.event(background=True)
    async def delete_person(self, user_id: int):
        async with self:
            response = rq.delete(f"{BACKEND_URL}/delete/{user_id}", headers={"Content-Type": "application/json"})
            print(response.status_code)
            if response.status_code == 200:
                self.submission_status = "Delete user success"
                self.people = [person for person in self.people if person[0] != user_id]
            else:
                self.submission_status = "Delete user failed"
    
        


def show_person(person: List[Union[int, str, bool]]):
    """Show a person in a table row."""
    
    return rx.table.row(
        rx.table.cell(person[0]),
        rx.table.cell(person[1]),
        rx.table.cell(person[2]),
        rx.table.cell(person[3]),
        rx.table.cell(person[4]),
        rx.table.cell(person[5]),
        rx.table.cell(
            rx.cond(
               person[6],
               "Active",
               "Inactive" 
            )
            ),
        rx.table.cell(rx.button(
            "Delete",
            on_click=lambda: TableForEachState.delete_person(person[0]),
            color_scheme="red",
            )
        ),
    )


def tableUser():
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("ID"),
                rx.table.column_header_cell("Name"),
                rx.table.column_header_cell("Email"),
                rx.table.column_header_cell("Phone"),
                rx.table.column_header_cell("Department"),
                rx.table.column_header_cell("CC"),
                rx.table.column_header_cell("Active"),
                rx.table.column_header_cell("Delete"),
            ),
            #align="center",
            style={
                "background-color": "gray",
                "color": "white",
                "font-size": "20px",
                },
            
        ),
        rx.table.body(
            rx.foreach(
                TableForEachState.people,
                lambda person: show_person(person),
            ),
            width="100%",
        ),
        width="70%",
        margin="auto",
        padding="2em",
        box_shadow="0, 0, 10px, 0, black",
        border_radius="lg",
        on_mount=TableForEachState.fetch_people,
    )
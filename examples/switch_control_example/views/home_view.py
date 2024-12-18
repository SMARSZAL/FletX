import flet as ft 
from fletx import Xview
from fletx.controls import Switch

class HomeView(Xview):

    def build(self):
        return ft.View(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                Switch(
                    ref=self.state.switch,
                    default="one",
                    controls={
                        "one":ft.Text("One",size=30),
                        "two":ft.Text("Two",size=30),
                        "three":ft.Text("Three",size=30),
                    }
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.ElevatedButton("Set one",on_click=self.state.set_one),
                        ft.ElevatedButton("Set two",on_click=self.state.set_two),
                        ft.ElevatedButton("Set three",on_click=self.state.set_three),
                    ]
                )
            ]
        )
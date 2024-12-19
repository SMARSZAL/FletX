import flet as ft 
from fletx import Xview

class HomeView(Xview):

    def init(self):
        # inject function in state
        self.state.inject_in_state(self.card_builder)

    def card_builder(self,text):
        return ft.Container(
            border_radius= 20,
            bgcolor=ft.colors.BLUE,
            content=ft.Text(text,size=30),
            alignment=ft.alignment.center,
            )

    def build(self):
        return ft.View(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.TextField(
                            label="write text hire",
                            ref=self.state.text
                            ),
                        ft.ElevatedButton("Add",on_click=self.state.add)
                    ]
                ),
                ft.Column(
                    ref=self.state.data,
                    alignment=ft.MainAxisAlignment.CENTER
                ),
            ]
        )
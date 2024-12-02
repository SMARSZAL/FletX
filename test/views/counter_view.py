import flet as ft 
from fletx import Xview

class CounterView(Xview):

    def build(self):
        return ft.View(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Row(
                    [
                        ft.IconButton(ft.Icons.REMOVE, on_click=self.state.minus_click),
                        self.state.txt_number,
                        ft.IconButton(ft.Icons.ADD, on_click=self.state.plus_click),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.ElevatedButton("<< Back",on_click=self.back)
            ]
        )
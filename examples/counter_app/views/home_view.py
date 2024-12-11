import flet as ft 
from fletx import Xview

class HomeView(Xview):

    def build(self):
        return ft.View(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Text("Home View"),
                ft.Text(f"Counts = {self.state.txt_number.value}"),
                ft.ElevatedButton("Go Counter View",on_click=lambda e:self.page.go("/counter"))
            ]
        )
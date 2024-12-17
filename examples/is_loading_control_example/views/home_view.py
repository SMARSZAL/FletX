import flet as ft 
from fletx import Xview
from fletx.controls import IsLoading

class HomeView(Xview):

    def build(self):
        return ft.View(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                IsLoading(
                    ref=self.state.loading,
                    loading_control=ft.ProgressRing(visible=True),
                    loaded_control=ft.Text("Data Is Loaded :)",size=30),
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.ElevatedButton("Set Data Is Loaded",on_click=self.state.setFalse),
                        ft.ElevatedButton("Set Data Is Loading",on_click=self.state.setTrue),
                    ]
                )
            ]
        )
from fletx import Xview
import flet as ft 


class DashboardView(Xview):
    
    def build(self):
        return ft.View(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Text("Wellcome To Dashboard",size=30),
                ft.ElevatedButton("Logout",on_click=self.state.logout)
            ]
        )

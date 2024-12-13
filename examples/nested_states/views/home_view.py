import flet as ft 
from fletx import Xview

class HomeView(Xview):

    def build(self):
        return ft.View(
            controls=[
                ft.Text(self.state.data),
                ft.Text(self.state.one.data),
                ft.Text(self.state.two.data),
            ]
        ) 
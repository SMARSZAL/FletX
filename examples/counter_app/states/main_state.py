from fletx.xstate import Xstate
import flet as ft 


class MainState(Xstate):
    def __init__(self, page):
        super().__init__(page)
        
        self.txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def minus_click(self,e):
        self.txt_number.value = str(int(self.txt_number.value) - 1)
        self.update()

    def plus_click(self,e):
        self.txt_number.value = str(int(self.txt_number.value) + 1)
        self.update()
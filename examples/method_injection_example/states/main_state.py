from fletx.xstate import Xstate
import flet as ft 


class MainState(Xstate):
    def __init__(self, page):
        super().__init__(page)
        
        self.data = ft.Ref[ft.Column]()
        self.text = ft.Ref[ft.TextField]()

    def add(self,e):
        self.data.current.controls.append(self.card_builder(self.text.current.value))
        self.text.current.value = ""
        self.update()
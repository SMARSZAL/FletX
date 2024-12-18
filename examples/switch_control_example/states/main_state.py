from fletx.xstate import Xstate
import flet as ft 
from fletx.controls import Switch

class MainState(Xstate):
    def __init__(self, page):
        super().__init__(page)
        
        self.switch = ft.Ref[Switch]()

    def set_one(self,e):
        self.switch.current.active = "one"
        self.update()

    def set_two(self,e):
        self.switch.current.active = "two"
        self.update()

    def set_three(self,e):
        self.switch.current.active = "three"
        self.update()

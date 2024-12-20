from flet import Ref
from fletx import Xstate
from fletx.controls import Switch

class MainState(Xstate):
    def __init__(self, page):
        super().__init__(page)
        
        self.nav_switch = Ref[Switch]()

    def change_nav(self,e):
        self.nav_switch.current.active = str(e.control.selected_index)
        self.update()



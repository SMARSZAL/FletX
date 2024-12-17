from fletx.xstate import Xstate
import flet as ft 
from fletx.controls import IsLoading


class MainState(Xstate):
    def __init__(self, page):
        super().__init__(page)
        
        self.loading = ft.Ref[IsLoading]()

    def setTrue(self,e):
        self.loading.current.is_loading = True
        self.update()

    def setFalse(self,e):
        self.loading.current.is_loading = False
        self.update()
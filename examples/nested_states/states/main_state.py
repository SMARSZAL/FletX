from fletx import Xstate
from .one_state import OneState
from .two_state import TwoState

class MainState(Xstate):
    def __init__(self, page):
        super().__init__(page)

        self.one = OneState(page)
        self.two = TwoState(page)

        self.data = "i am from Main State"


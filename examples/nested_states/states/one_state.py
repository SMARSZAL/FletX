from fletx import Xstate

class OneState(Xstate):
    def __init__(self, page):
        super().__init__(page)

        self.data = "i am from One State"

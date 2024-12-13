from fletx import Xstate

class TwoState(Xstate):
    def __init__(self, page):
        super().__init__(page)

        self.data = "i am from Two State"

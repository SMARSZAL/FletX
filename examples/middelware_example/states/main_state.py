from fletx import Xstate
from flet import Ref,TextField

class MainState(Xstate):
    def __init__(self, page):
        super().__init__(page)

        self.username = Ref[TextField]()
        self.password = Ref[TextField]()

        self.is_authenticated = False

    def login(self,e):
        if self.username.current.value == "saurabh" and self.password.current.value == "1234":
            self.is_authenticated = True
            self.go("/dashboard")
        else:
            self.username.current.error_text = "Invalid Username Or Password"
            self.password.current.error_text = "Invalid Username Or Password"
            self.update()
        
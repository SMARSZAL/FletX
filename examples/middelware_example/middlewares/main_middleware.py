from fletx import Xmiddleware

class MainMiddleware(Xmiddleware):

    def middleware(self):
        
        if self.is_route_match("/dashboard"):
            if self.state.is_authenticated != True:
                self.redirect_route("/")

        if self.is_route_match("/"):
            if self.state.is_authenticated:
                self.redirect_route("/dashboard")


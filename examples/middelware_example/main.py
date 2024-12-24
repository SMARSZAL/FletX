import sys
sys.path.append('../../')

import flet as ft 
from fletx import Xapp,route
from states.main_state import MainState
from views.login_view import LoginView
from views.dashboard_view import DashboardView
from middlewares.main_middleware import MainMiddleware

def main(page:ft.Page):
    page.title = "Flet & FletX Middleware Example"

    Xapp(
        page=page,
        state=MainState,
        middleware=MainMiddleware,
        routes=[
            route(route="/",view=LoginView),
            route(route="/dashboard",view=DashboardView)
        ]
    )
    
ft.app(target=main)



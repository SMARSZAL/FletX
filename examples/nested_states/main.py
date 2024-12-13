import sys
sys.path.append('../../')


import flet as ft 
from fletx import Xapp,route
from states.main_state import MainState
from views.home_view import HomeView

def main(page:ft.Page):
    page.title = "Loding"

    Xapp(
        page=page,
        init_route="/",
        state=MainState,
        routes=[
            route("/",HomeView)
        ]
    )

ft.app(main)
ft.app(main)
ft.app(main)
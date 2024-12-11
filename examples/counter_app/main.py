import sys
sys.path.append('../../')

import flet as ft
from fletx import Xapp,route
from states.main_state import MainState
from views.home_view import HomeView
from views.counter_view import CounterView

def main(page: ft.Page):
    page.title = "FletX counter example"

    Xapp(
        page=page,
        init_route="/",
        state=MainState,
        routes=[
            route(route="/",view=HomeView),
            route(route="/counter",view=CounterView),
        ]
    )

ft.app(main)
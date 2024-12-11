import sys
sys.path.append('../../')

import flet as ft 
from fletx import Xapp,route
from states.main_state import MainState
from views.home_view import HomeView
from views.edit_note_view import EditNoteView

def main(page:ft.Page):
    page.title = "FletX Note App"

    Xapp(
        page=page,
        state=MainState,
        init_route="/",
        routes=[
            route(route="/",view=HomeView),
            route(route="/edit_note/:note_title",view=EditNoteView),
        ],
    )


ft.app(main)
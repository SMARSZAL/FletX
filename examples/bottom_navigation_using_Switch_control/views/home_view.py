import flet as ft 
from fletx import Xview
from fletx.controls import Switch

class HomeView(Xview):

    def build(self):
        return ft.View(
            appbar=ft.AppBar(
                title=ft.Text("Flet & FletX - Bottom navigation"),
                center_title=True,
                bgcolor=ft.Colors.BLACK12,
                shape=ft.NotchShape.CIRCULAR,
            ),
            navigation_bar = ft.CupertinoNavigationBar(
                bgcolor=ft.Colors.BLACK12,
                inactive_color=ft.Colors.GREY,
                active_color=ft.Colors.WHITE,
                on_change=self.state.change_nav,
                destinations=[
                    ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Home"),
                    ft.NavigationBarDestination(icon=ft.Icons.COMMUTE, label="Commute"),
                    ft.NavigationBarDestination(
                        icon=ft.Icons.BOOKMARK_BORDER,
                        selected_icon=ft.Icons.BOOKMARK,
                        label="Explore",
                    ),
                ]
            ),
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                Switch(
                    ref=self.state.nav_switch,
                    controls={
                        "0":ft.Column(
                            expand=True,
                            controls=[
                                ft.Text("Home",size=30),
                                ft.ElevatedButton("Go Next View",on_click=lambda e:self.go("/next"))
                                
                            ]
                        ),
                        "1":ft.Text("Commute",size=30),
                        "2":ft.Text("Explore",size=30),
                    }
                )
            ]
        )
    

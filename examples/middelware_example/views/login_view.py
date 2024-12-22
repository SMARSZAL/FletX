from fletx import Xview
import flet as ft 

class LoginView(Xview):

    def build(self):
        return ft.View(
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text("Login",size=30),
                ft.Container(
                    width=300,
                    content=ft.Column(
                        controls=[
                            ft.TextField(ref=self.state.username,label="Username"),
                            ft.TextField(ref=self.state.password,label="Password",password=True),
                            ft.Container(height=30),
                            ft.FilledButton("LogIn",on_click=self.state.login)
                        ]
                    )
                ),
                
            ]
        )
    


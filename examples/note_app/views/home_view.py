import flet as ft 
from fletx import Xview

class HomeView(Xview):

    def init(self):
        self.columnRef = ft.Ref[ft.Column]()
        self.title = ft.TextField(label="Title")
        self.note = ft.TextField(label="Note..",multiline=True)
        self.dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Create New Note"),
            content=ft.Column(
                controls=[
                    self.title,
                    self.note,
                ]
            ),
            actions=[
                ft.TextButton("Save",on_click= lambda e: self.saveNote()),
                ft.TextButton("Cancel", on_click=lambda e:self.page.close(self.dlg_modal)),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

    def onBuildComplete(self):
        self.setAllNotesCard()
        
    def saveNote(self):
        self.state.createNote(title=self.title.value,note=self.note.value)
        self.title.value = ""
        self.note.value = ""
        self.page.close(self.dlg_modal)
        self.setAllNotesCard()

    def setAllNotesCard(self):
        self.columnRef.current.controls.clear()
        for i in self.state.notes:
            self.columnRef.current.controls.append(
                ft.Container(
                    on_click=lambda e,title=i: self.go(f"/edit_note/{title}"),
                    content=ft.Row(
                        controls=[
                            ft.IconButton(icon=ft.icons.DELETE,on_click=lambda e,title=i: (self.state.deleteNote(title),self.setAllNotesCard())),
                            ft.Text(i)
                        ]
                    )
                )
            )
        self.update()

    def build(self):
        return ft.View(
            appbar=ft.AppBar(
                title=ft.Text("FletX Note App"),
                center_title=True,
            ),
            floating_action_button=ft.FloatingActionButton(icon=ft.Icons.ADD,on_click=lambda e:self.page.open(self.dlg_modal)),
            controls=[ft.Column(ref=self.columnRef)]
        )

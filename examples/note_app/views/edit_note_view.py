import flet as ft 
from fletx import Xview

class EditNoteView(Xview):

    def init(self):
        self.title = ft.TextField(label="title",value=self.params.get("note_title"))
        self.note = ft.TextField(label="note",value=self.state.notes[self.params.get("note_title")],multiline=True)

    def build(self):
        return ft.View(
            floating_action_button=ft.FloatingActionButton(icon=ft.Icons.SAVE,
                on_click=lambda e: self.state.updateNote(old_title=self.params.get("note_title"),
                                                         title=self.title.value,
                                                         note=self.note.value)),
            appbar=ft.AppBar(
                leading=ft.IconButton(icon=ft.icons.ARROW_BACK,on_click=self.back),
                title=ft.Text(self.params.get("note_title")),
                center_title=True,
            ),
            controls=[
                self.title,
                self.note
            ]
        )

from fletx import Xstate

class MainState(Xstate):
    def __init__(self, page):
        super().__init__(page)

        self.notes = {}

    def createNote(self,title,note):
        self.notes[title] = note

    def updateNote(self,old_title,title,note):
        del self.notes[old_title]
        self.notes[title] = note

    def deleteNote(self,title):
        del self.notes[title]
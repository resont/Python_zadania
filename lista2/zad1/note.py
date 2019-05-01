import datetime

class Note:

    last_id = 0

    def __init__(self,text,tag):
        self.text = text
        self.tag = tag
        self.date = datetime.datetime.now()
        self.id = Note.last_id
        Note.last_id += 1

    def match(self,compare):
        if compare in self.text or compare in self.tag:
            return True
        else:
            return False

    def __str__(self):
        return f"Tytuł: {self.tag} Treść: {self.text}"
    
class Notebook(Note):

    def __init__(self):
        self.notes = []

    def new_note(self):
        tag = input("Podaj tytuł notatki: ")
        text = input("Podaj trść notatki: ")

        if tag and text:
            self.notes.append(Note(text,tag))
        else:
            print("Któryś z atrybutów jest pusty!")

    def modify_tag(self):
        note = self.note_id()
        tag = input("Podaj nowy tag: ")
        note.tag = tag

    def modify_text(self):
        note = self.note_id()
        text = input("Podaj nowy text: ")
        note.text = text

    def search(self):
        string = input("Podaj tekst do wyszukania: ")
        contains_string = []
        for note in self.notes:
            if note.match(string):
                contains_string.append(str(note))
        return contains_string

    def note_id(self):
        id = input("Podaj id notatki: ")
        

        for note in self.notes:
            if int(id) == note.id:
                return note

        


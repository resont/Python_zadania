import sys
from note import Note, Notebook

class Menu:
    def __init__(self):
        self.notebook = Notebook()
        self.options = {
            "1" : self.show_notes,
            "2" : self.search_notes,
            "3" : self.add_note,
            "4" : self.modify_note,
            "5" : self.quit
        }
    
    def show_menu(self):
        for option, command in self.options.items():
            print(f"{option} : {str(command)}")
    
    def show_notes(self):

        for note in self.notebook.notes:
            print(f"{note}\n")
    
    def search_notes(self):
        found_list = self.notebook.search()
        print(found_list)

    def add_note(self):
        self.notebook.new_note()

    def modify_note(self):
        option = input("Co chcesz edytować?\n1 : Edytuj tytuł\n2 : Edytuj tekst\n")
        if option == '1': 
            self.notebook.modify_tag()
        elif option == '2':
            self.notebook.modify_text()
        else:
            print("Nie ma takiej opcji!")

    def quit(self):
        sys.exit(0)

    def run(self):
        while True:
            self.show_menu()
            choice = input("Wybierz opcję: ")

            if choice in self.options:
                self.options[choice]()
            else:
                print("Nie ma takiej opcji!")

menu = Menu()
menu.run()
class Person:
    def __init__(self):
        self.name_setter()
        self.surname_setter()
        self.age_setter()

    def __str__(self):
        return f"Imie: {self.name} | Nazwisko: {self.surname} | Wiek: {self.age}"

    def name_setter(self):

        name = input("Podaj imię:   ")
        self.name = name

    def surname_setter(self):

        surname = input("Podaj nazwisko:    ")
        self.surname = surname

    def age_setter(self):

        age = input("Podaj wiek:    ")
        self.age = age

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname
    
    @property
    def age(self):
        return self.__age

    @name.setter
    def name(self,name):
        
        if len(name) >= 3:
            self.__name = name
        else:
            self.__name = "brak imienia"
    
    @surname.setter
    def surname(self,surname):
        
        if len(surname) >= 3:
            self.__surname = surname
        else:
            self.__surname = "brak nazwiska"

    @age.setter
    def age(self,age):
        
        if int(age) > 0 and int(age) < 130:
            self.__age = age
        else:
            self.__age = "brak wieku"

class Student(Person):
    def __init__(self):
        super().__init__()
        self.field_of_study_setter()
        self.student_book = {}
        self.student_book_setter()

    def __str__(self):
        return super().__str__() + f" | Kierunek:  {self.field_of_study} | {self.student_book}"
        
    def field_of_study_setter(self):
        field = input("Podaj kierunek studiów:  ")
        if field:
            self.field_of_study = field
        else:
            self.field_of_study = "brak danych"

    @property
    def field_of_study(self):
        return self.__field_of_study

    @field_of_study.setter
    def field_of_study(self,field):
        self.__field_of_study = field

    def student_book_setter(self):
        while True:
            subject = input("Podaj nazwę przedmiotu lub wpisz end, żeby wyjść:  ")

            if subject == "end":
                break
            else:
                grade = float(input(f"Podaj ocenę z przedmiotu {subject}:   "))
                self.student_book[subject] = grade

class Employee(Person):
    def __init__(self):
        super().__init__()
        self.job_title_setter()
        self.skills = []
        self.skills_setter()

    def __str__(self):
        return super().__str__() + f" | Stanowisko: {self.job_title} | Umiejętności: {self.skills}"

    @property
    def job_title(self):
        return self.__job_title

    @job_title.setter
    def job_title(self,job):
        if job:
            self.__job_title = job
        else:
            self.__job_title = "brak danych"
    
    def job_title_setter(self):
        job = input("Podaj stanowisko pracy:    ")
        self.job_title = job

    def skills_setter(self):
        print("Wpisz end, żeby wyjść")
        while True:
            skill = input("Podaj umiejętność:   ")

            if skill == "end":
                break
            else:
                self.skills.append(skill)

if __name__ == "__main__":

    ob1 = Student()
    print(ob1)

    ob2 = Employee()
    print(ob2)



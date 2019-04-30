class Pet:
    def __init__(self,name):
        self._name = name
        self.hunger = 0
        self.tiredness = 0
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        if len(name) >= 3:
            self._name = name
        else:
            print("Za krótkie imię!")
    
    def _passage_of_time(self):
        self.hunger += 1
        self.tiredness += 1

    
    def mood(self):
        if self.hunger < 5 and self.tiredness < 5:
            return "Zwierzak jest szczęśliwy"
        elif self.hunger >= 5 and self.hunger <= 10 and self.tiredness >= 5 and self.tiredness <= 10:
            return "Zwierzak jest zadowolony"
        elif self.hunger >= 11 and self.hunger <= 15 and self.tiredness >= 11 and self.tiredness <= 15:
            return "Zwierzak jest podenerowany"
        elif self.hunger > 15 and self.tiredness > 15:
            return "Zwierzak jest wściekły"    
    def talk(self):
        self.mood()
        self._passage_of_time()

    def eat(self,food=4):
        self.hunger -= food
        self._passage_of_time()

    def play(self,fun=4):
        self.tiredness -= fun
        self._passage_of_time()


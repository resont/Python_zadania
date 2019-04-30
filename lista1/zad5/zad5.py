class RocketEngine:
    count = 0
    all_power = 0
    def __init__(self,name,power):
        self.name = name
        self.power = power
        self.working = False
        RocketEngine.count += 1
    
    def start(self):
        if self.working == False:
            self.working = True
            RocketEngine.all_power += self.power

    def stop(self):
        if self.working:
            self.working = False
            RocketEngine.all_power -= self.power
    
    def __str__(self):
        return f"Nazwa silnika: {self.name}\nMoc silnika: {self.power}\nStatus: {self.working}\n"
    @staticmethod
    def __del__():
        RocketEngine.count -= 1
    @staticmethod
    def status():
        print(f"count: {RocketEngine.count}\nall_power: {RocketEngine.all_power}\n")

manewr = RocketEngine("manewr",50)
manewr.start()
print(manewr)
manewr.status()
manewr.stop()
del(manewr)

rozped = RocketEngine("rozped",500)
rozped.start()
print(rozped)
rozped.status()
rozped.stop()
del(rozped)

hiper = RocketEngine("rozped",4000000)
hiper.start()
print(hiper)
hiper.status()
hiper.stop()
del(hiper)



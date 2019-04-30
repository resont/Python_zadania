import weakref
class RocketEngine:
    count = 0
    all_power = 0
    def __init__(self, name, power):
        self.name = name
        self.power = power
        self.working = False
        RocketEngine.count += 1
    def start(self):
        if(self.working == False):
            self.working = True
            RocketEngine.all_power += self.power
            print(f"Engine: "+self.name +" with power lvl of: "+str(self.power)+" has been activated")
        else:
            print(f"Engine: "+self.name +" with power lvl of: "+str(self.power)+" is already working")
    def stop(self):
        if(self.working == True):
            self.working =  False
            RocketEngine.all_power -= self.power
            print(f"Engine: "+self.name +" with power lvl of: "+str(self.power)+" has been deactivated")
        else:
            print(f"Engine: "+self.name +" with power lvl of: "+str(self.power)+" is already deactivated")
    def __str__(self):
        return "Engine name: {n}, power: {p}, working: {w} ".format(n=self.name, p=self.power, w=self.working)
    def __del__(self):
        RocketEngine.count  = RocketEngine.count - 1
    def status():
        print(f"Number of all engines: " + str(RocketEngine.count)+ ", combined power: "+ str(RocketEngine.all_power))


SEngine1 = RocketEngine("Small engine 1",50)
SEngine1_wr =weakref.proxy(SEngine1)

SEngine2 = RocketEngine("Small engine 2",50)
SEngine2_wr =weakref.proxy(SEngine2)

Engine1 = RocketEngine("Engine 1",500)
Engine1_wr = weakref.proxy(Engine1)

Engine2 = RocketEngine("Engine 2",500)
Engine2_wr = weakref.proxy(Engine2)


HEngine1 = RocketEngine("Hyper Engine 1",400000)
HEngine1_wr = weakref.proxy(HEngine1)

HEngine2 = RocketEngine("Hyper Engien 2",400000)
HEngine2_wr = weakref.proxy(HEngine2)

print()

print("New spaceship has been created")
print()


#Manewry i te sprawy
print("Setting maneuver speed...")
SEngine1_wr.start()
SEngine2_wr.start()

print()

#Prędkość podświetlna
print("Engaging sublight engines...")

Engine1_wr.start()
Engine2_wr.start()

SEngine1_wr.stop()
SEngine2_wr.stop()
print()

#Wejście do hiperprzestrzeni
print("Entering hyperspeed ...")
HEngine1_wr.start()
HEngine2_wr.start()
print()

Engine1_wr.stop()
Engine2_wr.stop()
print()
print("+=Checking current status=+")
RocketEngine.status()

print()

#Wyjście z hyper speed
print("Leaving hyper Speed ...")
Engine1_wr.start()
Engine2_wr.start()
print()

HEngine1_wr.stop()
HEngine2_wr.stop()

print() 
print("---Dematerializing hyper engines")
print()

del HEngine1
del HEngine2
print()

#Dotarcie do portu
print("Entering Spaceport: Engaging maneuver engines...")
print()

SEngine1_wr.start()
SEngine2_wr.start()

Engine1_wr.stop()
Engine2_wr.stop()
print()

print("---Dematerializing sublight engines")
del Engine1
del Engine2

#Dokowanie
print()

print("Docking....")
print()

SEngine1.stop()
SEngine2.stop()
print()

print(" +++ Your spacecraft has been docked")

print()


print("---Dematerializing maneuver engines")
print()
del SEngine1
del SEngine2

print()

print("+=Checking current status=+")
RocketEngine.status()
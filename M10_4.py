import random
#ALL TASKS
class Car:
    regis=0
    maxsp=0
    def __init__(self, reg, maxs):
        self.regis = reg
        self.maxsp = maxs 
    speed=0
    distance=0
    def __str__(self):
        return f"Registration number: {self.regis:7s}| top speed: {self.maxsp:4d}| current speed: {self.speed:4d} | odometer: {self.distance}"
    def accelerate(self,changesp):
        self.speed+=changesp
        if (self.speed>self.maxsp):
            self.speed=self.maxsp
        elif(self.speed<0):
            self.speed=0    
    def drive(self, hours):
        self.distance+=hours*self.speed
class Race:
    name=0
    distance=0
    listc=[]
    def __init__(self,n,d,lst):
        self.name=n
        self.distance=d
        for i in lst:
            self.listc.append(i)
    def hour_passes(self):
        for i in range(0,len(self.listc)):
            self.listc[i].accelerate(random.randrange(-10, 16))
            self.listc[i].drive(1)
    def print_status(self):
        for i in range(0,len(self.listc)):
            print(self.listc[i])
    def race_finished(self):
        for i in range(0,len(self.listc)):
            if(self.listc[i].distance>=self.distance):
                return True
        return False
def main():
    listcars=[]
    for i in range(0,10):
        listcars.append(Car(f"ABC-{i+1}",random.randrange(100,201)))
    r1 = Race("Grand Demolition Derby",8000,listcars)
    counter=0
    while(r1.race_finished()==False):
        counter+=1
        r1.hour_passes()
        if(counter==10):
            counter=0
            r1.print_status()
    print()
    r1.print_status()
if __name__=="__main__":
    main()
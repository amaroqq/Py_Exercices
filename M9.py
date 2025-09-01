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
        return f"Car with registration number {self.regis}, top speed of {self.maxsp}, current speed of {self.speed} and a odometer indicating {self.distance}"
    def accelerate(self,changesp):
        self.speed+=changesp
        if (self.speed>self.maxsp):
            self.speed=self.maxsp
        elif(self.speed<0):
            self.speed=0    
    def drive(self, hours):
        self.distance+=hours*self.speed
def main():
    listcars=[]
    done = 0
    for i in range(0,10):
        listcars.append(Car(f"ABC-{i+1}",random.randrange(100,201)))
    newc=Car("ABC-123", 142)
    print(newc)
    newc.accelerate(30)
    print(newc.speed)
    newc.accelerate(70)
    print(newc.speed)
    newc.accelerate(50)
    print(newc.speed)
    newc.accelerate(-200)
    print(newc.speed)
    while(done==0):
        for i in range(0,10):
            listcars[i].accelerate(random.randrange(-10, 16))
            listcars[i].drive(1)
            if (listcars[i].distance==10000):
                done=1
    for i in range(0,10):
        print(listcars[i])
if __name__=="__main__":
    main()
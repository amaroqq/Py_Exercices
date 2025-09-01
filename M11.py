# Task 1
class Publication:
    name=''   
    def __init__(self, n):
        self.name=n
class Book(Publication):
        author=''
        pagec=0
        def __init__(self,a,p,n):
            super().__init__(n)
            self.author=a
            self.pagec=p
        def print_information(self):
            print(f"Name: {self.name}, author: {self.author}, page count: {self.pagec}")
class Magazine(Publication): 
        chiefed=''
        def __init__(self,c,n):
            super().__init__(n)
            self.chiefed=c
        def print_information(self):
            print(f"Name: {self.name}, chief editor: {self.chiefed}")
#Task 2
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
class ElectricCar(Car):
    capacitykwh=0
    def __init__(self,reg,maxs,c):
            super().__init__(reg,maxs)
            self.capacitykwh=c
class GasolineCar(Car):
    voltank=0
    def __init__(self,reg,maxs,v):
            super().__init__(reg,maxs)
            self.voltank=v

def main():
    p1=Magazine("Aki Hyyppä","Donald Duck")
    p2=Book("Rosa Liksom", 192, "Compartment No. 6")
    p1.print_information()
    p2.print_information()

    c1=ElectricCar("ABC-15",180,52.5)
    c2=GasolineCar("ACD-123",165,32.3)
    sp1=int(input("Enter speed for car 1: "))
    sp2=int(input("Enter speed for car 2: "))
    c1.accelerate(sp1)
    c2.accelerate(sp2)
    c1.drive(3)
    c2.drive(3)
    print(f"Odometer 1: {c1.distance}")
    print(f"Odometer 2: {c2.distance}")
if __name__=="__main__":
    main()
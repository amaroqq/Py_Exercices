import random
import math
#Task1
class Task_1:
    def __init__(self):
        pass
    def roll(self):
        return random.randrange(0,6)+1
    def main(self):
        num=self.roll()
        print(num)
        while(num != 6):
            num = self.roll()
            print(num)

#Task2
class Task_2:
    def __init__(self):
        pass
    def rollsides(self,sides):
        return random.randrange(0,sides)+1
    def main(self):
        sides = int(input("Enter a number: "))
        num = self.rollsides(sides)
        print(num)
        while(num != sides):
            num = self.rollsides(sides)
            print(num)

#Task3
class Task_3:
    def __init__(self):
        pass
    def GalToL(self,gal):
        return gal*3.78541
    def main(self):
        litres = int(input("Enter the volume in litres: "))
        while(litres>0):
            print(self.GalToL(litres))
            litres = int(input())

#Task4
class Task_4:
    def __init__(self):
        pass
    def suml(self,ls:list):
        sumz = 0
        for i in ls:
            sumz+=i
        return sumz
    def main(self):
        listus = [1,2,3,4]
        print(self.suml(listus))

#Task5
class Task_5:
    def __init__(self):
        pass
    def remodd(self,ls:list):
        y=len(ls)
        i = 0
        while(i<y):
            if (ls[i]%2==1):
                y-=1
                ls.pop(i)
                i-=1
            i+=1
        return ls

    def main(self):
        listus = [1,2,3,4]
        print(listus)
        print(self.remodd(listus))

#Task6
class Task_6:
    def __init__(self):
        pass
    def pizza(self,diam, price):
        area = math.pi*diam*diam/4
        return price/area*10000
    def main(self):
        p1 = int(input("Enter price of pizza 1: "))
        d1 = int(input("Enter diameter of pizza 1: "))
        p2 = int(input("Enter price of pizza 2: "))
        d2 = int(input("Enter diameter of pizza 2: "))
        if(self.pizza(d1,p1)<self.pizza(d2,p2)):
            print("Pizza 1 is better value for money")
        else:
            print("Pizza 2 is better value for money")
if __name__ == "__main__":
    Task_1().main()
    Task_2().main()
    Task_3().main()
    Task_4().main()
    Task_5().main()
    Task_6().main()




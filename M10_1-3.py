class Elevator:
    botf=0
    topf=0
    curf=0
    def __init__(self, b,t):
        self.botf=b
        self.topf=t
        self.curf=self.botf
    def floor_up(self):
        self.curf+=1
    def floor_down(self):
        self.curf-=1
    def go_to_floor(self,fl):
        if(fl<self.botf or fl>self.topf):
            print("Invalid destination!")
        else:
            if (self.curf>fl):
                self.floor_down()
                self.go_to_floor(fl)
            elif (self.curf<fl):
                self.floor_up()
                self.go_to_floor(fl)
            else:
                print("You have arrived!")
class Building:
    botf=0
    topf=0
    nelev=0
    listel =[]
    def __init__(self,b,t,e):
        self.botf=b
        self.topf=t
        self.nelev=e
        self.build()
    def build(self):
        for i in range(0,self.nelev):
            self.listel.append(Elevator(self.botf,self.topf))
    def run_elevator(self,num,dest):
        self.listel[num-1].go_to_floor(dest)
    def fire_alarm(self):
        for i in range(self.nelev):
            self.run_elevator(i+1,self.botf)
def main():
    el1=Elevator(0,5)
    el1.go_to_floor(3)
    el1.go_to_floor(0)
    b1=Building(0,3,3)
    for i in range(3):
        b1.run_elevator(i+1,3)
    b1.fire_alarm()

if __name__=="__main__":
    main()
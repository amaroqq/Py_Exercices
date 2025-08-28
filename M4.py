import random
#Task 1
num = 3
while (num<1000):
    if(num%3==0):
        print(f"{num}\n")
    num+=1
#Task 2
num = int(input("Enter a number in inches (or negative to skip): "))
while(num>=0):
    print(f"The value in centimeters is {num*2.54}")
    num = int(input())
#Task 3
num = input("Enter numbers to continue or an empty string to quit: ").strip()
checker = 0
if (num!=''):
    checker = 1
    maxs = int(num)
    mins = int(num)
while (num!=''):
    if (maxs<int(num)):
        maxs=int(num)
    if (mins>int(num)):
        mins=int(num)
    num = input().strip()
if(checker==1):
    print(f"The maximum is {maxs} and the minimum is {mins}")
#Task 4
num = random.randrange(1,11)
guess = int(input("Try to guess: "))
while (guess!=num):
    if (guess>num):
        print("Too high!")
    else:
        print("Too low!")
    guess = int(input())
print("Correct!")
# Task 5
usr = input("Enter Username: ")
pas = input("Enter Password: ")
cnt=1
while (((usr!='python')or(pas!='rules'))and cnt<5):
    print("Enter Username and Password again: ")
    usr = input()
    pas = input()
    cnt+=1
if (cnt==5):
    print("Acces Denied")
else:
    print("Welcome")
# Task 6
total = 0
inside = 0
total = int(input("How many total points shall there be? "))
cnt = 0
while (cnt<total):
    px = float(random.randrange(0,100000001))
    py = float(random.randrange(0,100000001))
    px /= 100000000
    py /= 100000000
    if ((px*px+py*py)<1):
        inside+=1
    cnt+=1
print(4*inside/total)
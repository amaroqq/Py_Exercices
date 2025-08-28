import random
import math
def isPrime(numbah):
    for i in range(2,math.trunc(math.sqrt(numbah))+1):
        if (numbah%i==0):
            return 0
    return 1
#Task 1
numdice = int(input("Enter the number of dice: "))
sum=0
for cnt in range(0,numdice):
    sum+=random.randrange(1,7)
print(f"The sum is {sum}")
#Task 2
nums = []
numinput = input("Enter numbers to continue or an empty string to quit: ").strip()
checker = 0
while (numinput!=''):
    nums.append(int(numinput))
    checker+=1
    numinput=input().strip()
if(checker<5):
    print(f"You didn't input 5 numbers")
else:
    nums.sort(reverse=True)
    print(nums[0:5])
#Task 3
numinput = int(input("Enter a number in the prime checker: "))
if (isPrime(numinput)==1):
    print("It is indeed a prime number")
else:
    print("It is not a prime number")
#Task 4
cityl=[]
for i in range(0,5):
    city=input("Enter the name of the city: ")
    cityl.append(city)
for c in cityl:
    print(f"{c}")
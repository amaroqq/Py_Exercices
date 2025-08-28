from math import pi
import random
# Task 1
name = input("Enter your name: ")
print("Hello, " + name)
#Task 2
radius = input("Enter the radius of the circle: ")
area = pi * float(radius) * float(radius)
print(f"The area of the circle is: {area:.2f}")
#Task 3
length = input("Enter length of a rectangle: ")
width = input("Enter width of a rectangle: ")
area = int(length) * int(width)
perim = 2 * (int(length) + int(width))
print(f"The perimeter of the rectangle is: {perim}")
print(f"The area of the rectangle is: {area}")
#Task 4
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
num3 = input("Enter the third number: ")
average = (int(num1) + int(num2) + int(num3)) / 3
print(f"The sum of the three numbers is: {int(num1) + int(num2) + int(num3)}")
print(f"The product of the three numbers is: {int(num1) * int(num2) * int(num3)}")
print(f"The average of the three numbers is: {average}")
#Task 5
w1 = input("Enter the first weight in talents: ")
w2 = input("Enter the second weight in pounds: ")
w3 = input("Enter the third weight in lots: ")
mass  = ((float(w1) * 20 + float(w2)) * 32 + float(w3))*13.3
print(f"The weight in modern units is {int(mass/1000)} kilograms and {mass-int(mass/1000)*1000:.2f} grams")
#Task 6
code1 = f"{random.randrange(0,10)}{random.randrange(0,10)}{random.randrange(0,10)}"
code2 = f"{random.randrange(1,7)}{random.randrange(1,7)}{random.randrange(1,7)}{random.randrange(1,7)}"
print(f"The three digit code is {code1} and the four digit code is {code2}")
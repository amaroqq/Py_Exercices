#Task 1
length = int(input("Enter the length of the zander (in centimeters): "))
if (length<42):
    print(f"Release the zander because it is {42-length} centimeters under the limit")
#Task 2
cclass = input("Enter the cruise ship cabin class: ")
if (cclass == "LUX"):
    print("LUX: upper-deck cabin with a balcony.")
elif (cclass == "A"):
    print("A: above the car deck, equipped with a window.")
elif (cclass == "B"):
    print("B: windowless cabin above the car deck.")
elif (cclass == "C"):
    print("C: windowless cabin below the car deck.")
else:
    print("Invalid cabin class")
#Task 3
gender = input("Enter your biological gender: ")
hem = int(input("Enter your hemoglobin value (g/l): "))
if (gender == 'male'):
    if (hem>=134 and hem<=167):
        print("Your hemoglobin is normal.")
    elif (hem>167):
        print("Your hemoglobin is high.")
    else:
        print("Your hemoglobin is low.")
else:
    if (hem>=117 and hem<=155):
        print("Your hemoglobin is normal.")
    elif (hem>155):
        print("Your hemoglobin is high.")
    else:
        print("Your hemoglobin is low.")
#Task 4
year = int(input("Enter a year: "))
if ((year%4==0 and year%100!=0) or year%400==0):
    print("The selected year is a leap year")
else:
    print("The selected year is not a leap year")

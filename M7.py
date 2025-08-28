#Task 1
seasons = "spring","summer", "autumn", "winter"
numb = int(input("Enter the number of the month: "))
match numb:
    case 12|1|2:
        print(seasons[3])
    case 3|4|5:
        print(seasons[0])
    case 6|7|8:
        print(seasons[1])
    case 9|10|11:
        print(seasons[2])
#Task 2
name = input("Enter names or an empty string to quit: ").strip()
set1 = set()
set2 = set()
while(name!=''):
    set2.add(name)
    if(set1==set2):
        print("Existing name")
    else:
        set1.add(name)
        print("New name")
    
    name = input().strip()
for i in set1:
    print(i)
#Task 3
testinput=input("Enter 'New entry', 'Fetch entry' or 'Quit': ")
datab=dict()
exit=0
while(exit==0):
    match testinput:
        case "New entry"|"new entry":
            name=input("Enter the name: ")
            key=input("Enter the ICAO code: ")
            datab.update({key,name})
        case "Fetch entry"|"fetch entry":
            key=input("Enter the ICAO code: ")
            print(datab[key])
        case "Quit"|"quit":
            exit=1
        case _:
            print("You entered an undefined option. Try again. ")
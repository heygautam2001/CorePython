#verify year : normal or leap

Year = int(input("Enter year : \n"))

if (Year % 4 == 0 or Year % 400 ==0 ) and Year % 100 != 0:
    print("You entered a leap year" , Year)

else:
    print("You entered a non leap year " ,Year)


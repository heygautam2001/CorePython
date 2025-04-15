
number = int(input("Enter a number"))

for i in range (1 , 11):
    print( number , " * " , i , " = ", number*i)

print()

for i in range(1 , 11):
    if(i == 5):
        continue
    else:
        print(number, " * ", i, " = ", number * i)

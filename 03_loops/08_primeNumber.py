from curses.ascii import isprint

number = int(input("Enter a number : \n"))

isPrime = True

if number > 1:
    for i in range(2 , number):
        if(number % i) == 0:
            isPrime = False
            break
print(isPrime)
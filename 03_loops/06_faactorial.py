from math import factorial

num = int(input("Enter a number : \n"))
x = num
factorial = 1;

while num > 0:
    factorial = factorial * num
    num = num-1
print("Factorial of ",  x , " is ",factorial)

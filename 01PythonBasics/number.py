print(0o20)
print(0xFF)
print(0b1000)

print(oct(64))
print(hex(15))
print(bin(8))
print(3.14)

print(int('64' , 8))

print(int('1000' , 2))

import random

print(random.random()*10 + 1)

l1 = ['lemon' , 'masala' , 'ginger' , 'mint']
randomEle =  random.choice(l1)
print(randomEle)

print(random.shuffle(l1))

print((0.1 + 0.1 + 0.1 )- 0.3)#5.551115123125783e-17

from decimal import Decimal
y = Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
print(y)

from fractions import Fraction
myFra = Fraction(2,7)
print(myFra)

setOne = {1,2,3,4}
print(setOne & {1 , 3}) #intersection
print(setOne | {1 , 3 , 7}) #union

print(True + 4); #5
print(False + 4);#4

print(True is 1) #False
print(True is 0) #False
print(False is 1) #False
print(False is 0) #False


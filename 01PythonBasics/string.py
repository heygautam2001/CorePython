
"""  """
from traceback import print_tb

chai = "Lemon Chai"
print(chai)

chai = "Masala Chai"
print(chai)

char0 = chai[0]
print(char0)

sliceChai = chai[0:6]
print(sliceChai);

print(chai[0:12])

num_list = "0123456789"
print(num_list[:])
print(num_list[3:])
print(num_list[:7])
print(num_list[0:7:2])
print(num_list[0:7:3])
print(num_list[-1:])


print(chai.lower())
print(chai.upper())

tea = "   tea & tea   "
print(tea.strip())

print(tea.replace("tea" , "cofee"))


chai = "Lemon , Ginger , Masala , Mint"

print(chai.split())
print(chai.split(", "))

print(tea.find("&"))
print(tea.count("tea"))

chai_type = "Masala"
quantity = 2
order = "I ordered {} cups of {} chai"
print(order)
print(order.format(quantity , chai_type))

chai_variety = ["Lemon" , "Masala" , "Ginger"]
print("-".join(chai_variety))
print(len(chai))

for letter in chai:
    print(letter)


string = "he said  , \"Masala chai is awesome\""
print(string)

string2 = "Masala\nchai"
print(string2)

string2 = r"Masala\nchai"
print(string2)
print("Masala" in string2)
print("Chai" in string2);
print("Gautam" in string2)
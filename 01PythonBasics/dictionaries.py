from traceback import print_tb

chai_types = {"Masala" : "spicy" , "Ginger":"Zesty" , "Green" : "Mild"}
print(chai_types)

print(chai_types.get("Masala"))
print(chai_types.get("Mint"))


chai_types["Green"] = "FreshChai"
print(chai_types)

for chai in chai_types:
    print(chai , chai_types.get(chai));
print("\n")
for key , values in chai_types.items():
    print(key , values)

if "Masala" in chai_types:
    print(chai_types.get("Masala"))
else:
    print("Note Available")

chai_types["Earl grey"] = "Citrus"
print(chai_types)

chai_types.pop("Ginger");
print(chai_types);

chai_types.popitem();
print(chai_types)

del chai_types["Green"]
print(chai_types)

chai_types_copy = chai_types.copy();
print(chai_types_copy)
print("\n")
tea_shop = {
    "chai":{"Masala" : "Spicy" , "Ginger" : "Zesty"},
    "Tea" : {"Green" : "Mild" , "Black":"Strong"}

}
print(tea_shop)
print(tea_shop["chai"])
print(tea_shop["chai"]["Masala"])

squared_nums = {x:x**2 for x in range(6)}
print(squared_nums)
squared_nums.clear()
print(squared_nums)


keys = ["Masala" , "Ginger" , "Lemon"]
print(keys)
default_value = "Delicious"
new_dict = dict.fromkeys(keys , default_value)
print(new_dict)
new_dict = dict.fromkeys(keys , keys)
print(new_dict)
from traceback import print_tb

tea_types = ("Black" , "Green" , "Oolong" , "white" , "Red")
print(tea_types)
print(tea_types[0])
print(tea_types[2])
print(tea_types[1])

print(tea_types[-1:])
print(tea_types[0:3])
print(tea_types[0:6])

print(len(tea_types))

# tea_types[0] = "Herbal" # error
# print(tea_types)

more_tea = ("Herbal" , "Earl Grey")
all_tea = more_tea+tea_types
print(all_tea)

if("Green" in all_tea):
    print(" Say green")

print(more_tea.count("Earl Grey"))
print(all_tea.count("Herbal"))

# (black , green , Oolong) = tea_types
# print(tea_types)

print(type(tea_types))
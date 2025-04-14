from traceback import print_tb

tea_varieties = ["Black" , "Green" , "Onlong" , "White"]
print(tea_varieties)
print(tea_varieties[1]);
print(tea_varieties[-1])
print(tea_varieties[:3])
print(tea_varieties[2:])
print(tea_varieties[0: : 2])
tea_varieties[2] = "Herbal"
# tea_varieties[1:2] = "Lemon" #['Black', 'L', 'e', 'm', 'o', 'n', 'Herbal', 'White']
print(tea_varieties)
tea_varieties[1:2] = ["Lemon"]
print(tea_varieties)
print(tea_varieties[1:1]) #[]
tea_varieties[1:1] = ["test" , "test"];
print(tea_varieties)
print(tea_varieties[1:3])

tea_varieties[1:3] = []
print(tea_varieties)

for tea in tea_varieties:
    print(tea)

for tea in tea_varieties:
    print(tea , end="-")
print("\n")
if "Oolong" in tea_varieties:
    print("Oolong"+ "tea")
else:
    print("Nhi hai chai")


tea_varieties.append("Oolong");
print(tea_varieties);

tea_varieties.append("GaramMasala")
print(tea_varieties)

tea_varieties.pop()
print(tea_varieties)

tea_varieties.insert(1,"Green")
print(tea_varieties)

tea_varieties_copy = tea_varieties
print("tea_varieties_copy " ,tea_varieties_copy)

tea_varieties_copy = tea_varieties.copy()
print(tea_varieties)

tea_varieties_copy.append("LemonLeaf")
print(tea_varieties_copy);
print(tea_varieties)

print(range(0,10));
y = range(10);
print(y)

squared_nums = [x**2 for x in range(10)]
print(squared_nums)

cube_nums = [y**3 for y in range(10)]
print(cube_nums)
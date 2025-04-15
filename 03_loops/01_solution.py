numbers = [1 , -2 , 3 , -4 , 5, 6, -7, -8, 9, 10]

for nums in numbers:
    print(nums)

positive_count = 0

for nums in numbers:
    if nums > 0:
        positive_count += 1

print("Final count of positive number"  , positive_count)




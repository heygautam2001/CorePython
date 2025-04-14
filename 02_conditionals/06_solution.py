
distance = 20

if distance < 3:
    transport = "walk"
elif distance <= 15:
    transport = "Bike"
else:
    transport = "car"

print("Transport is " , transport)

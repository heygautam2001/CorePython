from fileinput import close

fruit = "Banana"
color = "Yellow"

if fruit == "Banana":
    if color == "Green":
        print("Unripe")
    elif color == "Brown":
        print("rotten")
    elif color == "Yellow":
        print("ripped")
        


day = str(input("Enter Day : "))
age = int(input("Enter your age : "))

movieTicketPrice = 12 if age >= 18 else 8

if day == 'wednesday':
    movieTicketPrice -= 2

print("Ticket price for you is $" ,movieTicketPrice)
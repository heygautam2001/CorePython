# password checker : easy  , medium , strong

noOfDigitInPassword = int(input("Enter you password lenght"))

if noOfDigitInPassword < 8:
    print("Your passowrd is easy to guess : ")
elif noOfDigitInPassword >= 8 and noOfDigitInPassword < 12:
    print("Your password is should not guesed easily")
else:
    print("Your password is hard to guess")


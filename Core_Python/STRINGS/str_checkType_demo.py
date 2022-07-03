s = input("Enter any Character :")
if s.isalnum():
    print("Alpha Numeric Character")
    if s.isalpha() :
        print("Alphabet Character")
        if s.islower() :
                print("Lower Case Alphabet Character")
        else :
                print("Upper Case Alphabet Character")
    else :
        print("It is Digit")
elif s.isspace() :
    print("It is Space Character")
else :
    print("Non Space Special Character")

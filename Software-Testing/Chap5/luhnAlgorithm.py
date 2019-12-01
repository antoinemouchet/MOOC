# concise definition of the Luhn checksum:
#
# "For a card with an even number of digits, double every odd numbered
# digit and subtract 9 if the product is greater than 9. Add up all
# the even digits as well as the doubled-odd digits, and the result
# must be a multiple of 10 or it's not a valid card. If the card has
# an odd number of digits, perform the same addition doubling the even
# numbered digits instead."
#
# for more details see here:
# http://www.merriampark.com/anatomycc.html
#
# also see the Wikipedia entry, but don't do that unless you really
# want the answer, since it contains working Python code!
# 
# Implement the Luhn Checksum algorithm as described above.


# is_luhn_valid takes a credit card number as input and verifies 
# whether it is valid or not. If it is valid, it returns True, 
# otherwise it returns False.
import random as r

def is_luhn_valid(n):
    # Check sum worked
    if checkSum(n) == 0:
        return True
    
    return False

def checkSum(number):
    number = str(number)

    # Counter variable at 0 (odd number of digits)
    counter = 0

    # Even number of digits
    if len(number) % 2 == 0:
        # Start counter at 1
        counter = 1

    # Final result
    result = 0

    for digit in number:
        # If digit is even (not in python but for real)
        if counter % 2 == 1:

            # Multiply digit by 2
            double = (2*int(digit))

            # Check if the double is greater than 10
            if double > 9:
                # Make double less than 10
                double -= 9

            # Increase result by number
            result += double

        # Just directly add odd digit to result
        else:
            result += int(digit)

        # Increase counter by 1
        counter += 1

    # Get the modulo 10 of the result
    result = result % 10

    return result

def generate(identifier, lenght):
    
    # Get number of digits to create
    counter = lenght - len(identifier) - 1

    assert counter > 0

    # We just have the identifier of the card number for the moment
    actNum = identifier

    # Fill card number
    while counter > 0:
        # Add a random digit 
        actNum += str(r.randrange(10))
        # Decrease counter
        counter -= 1

    # Finish number with 0
    actNum += "0"

    isOK = checkSum(actNum)

    # Number is invalid
    if isOK != 0:
        # Change it into a list to modify last digit
        actNum = list(actNum)
        # get size of actual number
        size = len(actNum)

        # change last digit to make it right
        actNum[size - 1] = str(10 - isOK)

        # Change back into a string
        actNum = "".join(actNum)
    
    return actNum


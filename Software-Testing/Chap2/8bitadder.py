# SPECIFICATION:
#
# add8 emulates an 8-bit hardware adder.
# it takes 17 bits, representing two 8-bit
# numbers and a carry bit.
#
# TASK:
#
# Write test() such that it achieves 100% 
# statement coverage of the add8 function.

def add8(a0,a1,a2,a3,a4,a5,a6,a7,b0,b1,b2,b3,b4,b5,b6,b7,c0):
    s1 = False
    if (a0 != b0) != c0:
        s1 = True
    c1 = False
    if (a0 and b0) != (c0 and (a0 != b0)):
        c1 = True
    s2 = False
    if (a1 != b1) != c1:
        s2 = True
    c2 = False
    if (a1 and b1) != (c1 and (a1 != b1)):
        c2 = True
    s3 = False
    if (a2 != b2) != c2:
        s3 = True
    c3 = False
    if (a2 and b2) != (c2 and (a2 != b2)):
        c3 = True
    s4 = False
    if (a3 != b3) != c3:
        s4 = True
    c4 = False
    if (a3 and b3) != (c3 and (a3 != b3)):
        c4 = True
    s5 = False
    if (a4 != b4) != c4:
        s5 = True
    c5 = False
    if (a4 and b4) != (c4 and (a4 != b4)):
        c5 = True
    s6 = False
    if (a5 != b5) != c5:
        s6 = True
    c6 = False
    if (a5 and b5) != (c5 and (a5 != b5)):
        c6 = True
    s7 = False
    if (a6 != b6) != c6:
        s7 = True
    c7 = False
    if (a6 and b6) != (c6 and (a6 != b6)):
        c7 = True
    s8 = False
    if (a7 != b7) != c7:
        s8 = True
    c8 = False
    if (a7 and b7) != (c7 and (a7 != b7)):
        c8 = True
    return (s1,s2,s3,s4,s5,s6,s7,s8,c8)


def convertTobinary(number):
    # List to store remainders
    remainders = []

    done = False
    # Loop until number is equal to 0
    while not done:
        # Get the result of the entire division and keep it
        result = number // 2
    
        # If result is 0 then we leave the loop
        if result == 0:
            done = True
    
        # Add remainder of division to the list of remainders
        remainders.append(number % 2)
    
        # Update number value
        number = result

    # Make it eight bit list
    while len(remainders) < 8:
        remainders.append(0)

    return (remainders[0], remainders[1], remainders[2], remainders[3], remainders[4],remainders[5], remainders[6], remainders[7])


def binToDec(d0,d1,d2,d3,d4,d5,d6,d7,lastDig):

    result = d0 * 1 + d1 * 2 + d2 * 4 + d3 * 8 + d4 * 16 + d5 * 32 + d6 * 64 + d7 * 128 + lastDig * 256

    return result

def test():

    for a in range (256):
        for b in range (256):
            
            (d0,d1,d2,d3,d4,d5,d6,d7) = convertTobinary(a)
            (e0,e1,e2,e3,e4,e5,e6,e7) = convertTobinary(b)
            (s0,s1,s2,s3,s4,s5,s6,s7, t) = add8(d0,d1,d2,d3,d4,d5,d6,d7,e0,e1,e2,e3,e4,e5,e6,e7, 0)

            print("%d + %d = %d" % (a, b, binToDec(s0,s1,s2,s3,s4,s5,s6,s7, t)))

test()


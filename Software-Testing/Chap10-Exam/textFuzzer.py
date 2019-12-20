# Fuzz Testing
# ------------
# Write a random fuzzer, based on Charlie Miller's example
# from Problem Set 4, for a text viewer application.
#
# For multiple iterations, the procedure, fuzzit, should take in the content
# of a text file, pass the content into a byte array, randomly modify bytes
# of the "file", and add the resulting byte array (as a String) to a list. 
# The return value of the fuzzit procedure should be a list of 
# byte-modified strings.


import random
import math

content = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Phasellus sollicitudin condimentum libero,
sit amet ultrices lacus faucibus nec.
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Cum sociis natoque penatibus et magnis dis parturient montes,
nascetur ridiculus mus. Cras nulla nisi, accumsan gravida commodo et,
venenatis dignissim quam. Mauris rutrum ullamcorper consectetur.
Nunc luctus dui eu libero fringilla tempor. Integer vitae libero purus.
Fusce est dui, suscipit mollis pellentesque vel, cursus sed sapien.
Duis quam nibh, dictum ut dictum eget, ultrices in tortor.
In hac habitasse platea dictumst. Morbi et leo enim.
Aenean ipsum ipsum, laoreet vel cursus a, tincidunt ultrices augue.
Aliquam ac erat eget nunc lacinia imperdiet vel id nulla."""


def fuzzit(content):

    # Fuzzing factor
    FuzzFactor = 1

    # Convert content to list of bytes
    contentAsBytes = bytearray(content)

    # Get number of bytes to corrupt
    NbCorrupt = random.randrange(math.ceil((float(len(contentAsBytes)) / FuzzFactor))) + 1
    
    # Loop until we corrupted chosen amount of bytes
    for byte in range(NbCorrupt):

        # Get a random byte
        rbyte = random.randrange(256)
        # Random bytes anywhere
        randIndex = random.randrange(len(contentAsBytes))

        # Change byte by random byte at position wanted
        contentAsBytes[randIndex] = "%c"%(rbyte)
    
    # Convert bytes array to string
    corruptedString = str(contentAsBytes)

    # Make it a list of string
    listCorruptedStrings = [corruptedString]

    # Return the list
    return listCorruptedStrings
    
# Write a random fuzzer for a simulated text viewer application

"""
Module with miscellaneous functions for the bio-informatic MOOC by coursera.
"""


def pattern_to_number(pattern):
    """
    Return a number based on the pattern inserted

    Parameters
    ----------
    pattern: the string to get the number for (str)

    Returns
    -------
    total: number based on the pattern (int)
    """
    dico = {"A": 0, "C": 1, "G": 2, "T": 3}

    total = 0

    # Loop on each letter of pattern
    for i, val in enumerate(pattern[::-1]):
        total += dico[val] * (4**i)

    return total

def numberToPattern(number, length):
    """
    Parameters
    ----------
    number: the number to convert (int)
    length: the length of the pattern (int)

    Returns
    -------
    pattern: corresponding pattern (str)

    """
    matching_letter = {0: "A", 1: "C", 2: "G", 3: "T"}
    pattern = ""
    # List to store remainders
    remainders = []

    done = False
    # Loop until number is equal to 0
    while not done:
        # Get the result of the entire division and keep it
        result = number // 4
    
        # If result is 0 then we leave the loop
        if result == 0:
            done = True
    
        # Add remainder of division to the list of remainders
        remainders.append(number % 4)
    
        # Update number value
        number = result

    # Reverse the list
    remainders.reverse()

    # Convert remainder to corresponding string that represents pattern
    for remainder in remainders:
        pattern += matching_letter[remainder]
    
    # Fill with A because 0 == A
    while len(pattern) < length:
        pattern = "A" + pattern

    return pattern

def getReverseComplement(initial):
    """
    Return the reverse complement of a DNA sequence.

    Parameters
    ----------
    initial: the dna sequence (str)

    Returns
    -------
    complement: the reverse complement of initial dna sequence (str)
    """

    complement = initial
    # Reverse complement
    complement.reverse()

    # Loop on every element to replace it by its complement
    for letter_id in range(len(complement)):

        if complement[letter_id] == "A":
            complement[letter_id] = "T"
        
        elif complement[letter_id] == "T":
            complement[letter_id] = "A"
        
        elif complement[letter_id] == "G":
            complement[letter_id] = "C"
        
        elif complement[letter_id] == "C":
            complement[letter_id] = "G"

    # Make it a string
    return "".join(complement)
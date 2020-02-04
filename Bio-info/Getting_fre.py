"""
Module for diverse operations on a string
"""

def get_text(file_path):
    """
    Returns text of file
    
    Parameters
    ----------
    file_path: path of file to get text from (str)

    Returns
    -------
    text: text from the file (str)
    """
    
    #Open file in reading mode
    text_file = open(file_path, 'r', encoding='ISO-8859-1')

    #Read file
    text = text_file.read()

    #Close file
    text_file.close()

    return text

def str_to_list(text):
    """
    Convert a string to a list.

    Parameters
    ----------
    text: a string (str)

    Returns
    -------
    text_list: a list with each element of text as 1 element

    """
    #Initialize list to contain elements of text
    text_list = []

    #Loop on every element of text
    for letter in text:

        #Add element to the list
        text_list.append(letter)
    
    return text_list

def get_freq_element(letters_list):
    """
    Returns a dictionary with frequence of each element in list

    Parameters
    -----------
    letters_list: list of symbols (list)

    Returns
    -------
    element_freq_dict: dict with frequence of appearance of each element of letters_list (dict)

    """
    #Initialize dico
    element_freq_dict = {}

    #Loop on element of list
    for symbol in letters_list:

        #Check that symbol's frequence is not already calculated and is not newline
        if symbol not in element_freq_dict.keys() and symbol != "\n":

            #Compute freq of appearance and add it into dictionary
            element_freq_dict[symbol] = letters_list.count(symbol) / len(letters_list)

    return element_freq_dict

def get_key_for_value(dict_of_elements, value_to_find, elements_found):
    """
    Returns the key's name of the value

    Parameters
    ----------
    dict_of_elements: dict with value to find in (dict)
    value_to_find: element to find in dict (str/int)
    elements_found: list of elements already found in dict (list) 

    Returns
    -------
    key: name of the key corresponding to value (str)

    """
    #Get all items of dict
    items_list = dict_of_elements.items()

    #Initialize loop
    found = False

    #Loop until letter is found
    while not found:

        #Loop on list of items
        for item  in items_list:

            #Check if value is the one looked for and check that we didn't already use the key
            if item[1] == value_to_find and item[0] not in elements_found:

                #Get key name and end the loop
                key = item[0]
                found = True

    return  key

def sort_dict_to_list(freq_dict):
    """
    Returns a list containing each element of initial text but
    sorted from element with highest apparition rate to least

    Parameters
    ----------
    freq_dict: dictionary with frequence of appearance of each element (dict)

    Returns
    -------
    sorted_list: list containing each element of initial text but
    sorted from element with highest apparition rate to least (list)
    """
    #get values of dict
    frequences = list(freq_dict.values())
    #Sort values in descreasing order
    frequences.sort(reverse=True)

    #Initialize sorted list and elements found
    sorted_list = []
    elements_found = []

    #Loop on every values descreasingly
    for freq in frequences:
        #Add the corresponding letter to the list 
        key = get_key_for_value(freq_dict, freq, elements_found)
        sorted_list.append(key)
        elements_found.append(key)

    return sorted_list

def patternCount(text, pattern):
    """
    Returns the number of times specified patter appears in text

    Parameters
    ----------
    text:text: the string in which we count the pattern (str)
    pattern: the pattern to look for (str)

    Returns
    -------
    count: number of times pattern appears in text (int)

    Notes
    -----
    This function works even tho strings are overlapping.
    """
	# Initialize count and start_id
    count = 0
    start_id = 0

    # Loop on every letter of the text
    while start_id < len(text): 

		# Check if pattern appears at least once
        index = text.find(pattern, start_id)
        if index != -1: 
			# If pattern is present then move the start_iding index
            start_id = index + 1

			# Increment the count 
            count += 1
        
        # Pattern doesn't appear anymore.
        else: 
            return count 

def freq_substring(text, length):
    """
    Returns the most frequent substring which is longer than min_length
    
    Parameters
    ----------
    text: the string in which we look for substrings (str)
    length: the number of letters in substrings (int)

    Returns
    -------
    freq_sub: list of frequent substring (str)
    """

    # Initialize list of frequent substring
    freq_sub = []
    max_count = 0

    # Loop on all letters of text
    for letter_id in range(len(text)-length):

        # Define actual substring
        substring = text[letter_id:letter_id + length]

        # Get number of times substring appears in text
        count = patternCount(text, substring)

        # Check if substring appears more than the actual maximum number of occurence 
        if count > max_count:
            freq_sub = [substring]

            # Update maximum occurence
            max_count = count
        
        # Substring appears as much as actual maximum
        elif count == max_count:
            freq_sub.append(substring)

    # Remove duplicates from list of substrings
    for element in freq_sub:
        while freq_sub.count(element) > 1:
            freq_sub.remove(element)

    return freq_sub


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

print(numberToPattern(5437, 8))

#print(freq_substring(get_text("./VibrioCholerae_ori.txt"), 9))

#print(sort_dict_to_list(get_freq_element(str_to_list(get_text('./VibrioCholerae_ori.txt')))))
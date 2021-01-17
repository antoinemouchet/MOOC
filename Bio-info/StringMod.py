"""
Module for diverse operations on a string
"""

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


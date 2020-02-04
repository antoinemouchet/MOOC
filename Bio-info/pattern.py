def readStartFile(filePath):
    """
    Returns the content of a file as a list. Each element of the list is a line.

    Parameters
    ----------
    filePath: the path of the file (str)

    Returns
    -------
    content: list of lines of files (list)
    """
    #Open file in reading mode
    text_file = open(filePath, 'r', encoding='ISO-8859-1')

    #Read file
    content = text_file.readlines()

    # Check there is only 2 lines
    if len(content) > 2:
        # Extract last line
        final = content[-1]

        # Make all others elements 1 element
        text = ""
        for line in content[:-1]:
            text += line

        # Define final value of content
        content = [text, final]

    #Close file
    text_file.close()

    return content

def readEndFile(filePath):
    """
    Returns the content of a file as a list. Each element of the list is a line.

    Parameters
    ----------
    filePath: the path of the file (str)

    Returns
    -------
    content: list of lines of files (list)
    """
    #Open file in reading mode
    text_file = open(filePath, 'r', encoding='ISO-8859-1')

    #Read file
    content = text_file.readlines()

    # Check there is only 2 lines
    if len(content) > 2:
        # Extract first line
        start = content[0]

        # Make all others elements 1 element
        text = ""
        for line in content[1:]:
            text += line

        # Define start value of content
        content = [start, text]

    #Close file
    text_file.close()

    return content

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

def findPatterns(text, length):
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

def patternIndexes(text, pattern):
    """
    Returns list of indexes where specified patter appears in text

    Parameters
    ----------
    text: text: the string in which we count the pattern (str)
    pattern: the pattern to look for (str)

    Returns
    -------
    pat_id: list of indexes where pattern appears in text (int)

    Notes
    -----
    This function works even tho strings are overlapping.
    """
	# Initialize start_id
    start_id = 0
    pat_id = []

    # Loop on every letter of the text
    while start_id < len(text): 

		# Check if pattern appears at least once
        index = text.find(pattern, start_id)
        if index != -1:
            # Append starting index of substring
            pat_id.append(index)
			# If pattern is present then move the start_iding index
            start_id = index + 1
        
        # Pattern doesn't appear anymore.
        else: 
            return pat_id


#analyzing = readStartFile("./ViChoFind.txt")
#ind_list = patternIndexes(analyzing[1].strip(), analyzing[0].strip())
#print(" ".join([str(elem) for elem in ind_list]))
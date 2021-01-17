"""
Module with operations to get content from a file.
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

def readStartFile(filePath):
    """
    Returns the content of a file as a list. [Content, last line]
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
    Returns the content of a file as a list. [first line, content]

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

# SPECIFICATION:
#
# check_sudoku() determines whether its argument is a valid Sudoku
# grid. It can handle grids that are completely filled in, and also
# grids that hold some empty cells where the player has not yet
# written numbers.
#
# First, your code must do some sanity checking to make sure that its
# argument:
#
# - is a 9x9 list of lists
#
# - contains, in each of its 81 elements, an integer in the range 0..9
#
# If either of these properties does not hold, check_sudoku must
# return None.
#
# If the sanity checks pass, your code should return True if all of
# the following hold, and False otherwise:
#
# - each number in the range 1..9 occurs only once in each row 
#
# - each number in the range 1..9 occurs only once in each column
#
# - each number the range 1..9 occurs only once in each of the nine
#   3x3 sub-grids, or "boxes", that make up the board
#
# This diagram (which depicts a valid Sudoku grid) illustrates how the
# grid is divided into sub-grids:
#
# 5 3 4 | 6 7 8 | 9 1 2
# 6 7 2 | 1 9 5 | 3 4 8
# 1 9 8 | 3 4 2 | 5 6 7 
# ---------------------
# 8 5 9 | 7 6 1 | 4 2 3
# 4 2 6 | 8 5 3 | 7 9 1
# 7 1 3 | 9 2 4 | 8 5 6
# ---------------------
# 9 6 1 | 5 3 7 | 0 0 0
# 2 8 7 | 4 1 9 | 0 0 0
# 3 4 5 | 2 8 6 | 0 0 0
# 
# Please keep in mind that a valid grid (i.e., one for which your
# function returns True) may contain 0 multiple times in a row,
# column, or sub-grid. Here we are using 0 to represent an element of
# the Sudoku grid that the player has not yet filled in.

# check_sudoku should return None
ill_formed = [[5,3,4,6,7,8,9,1,2],
              [6,7,2,1,9,5,3,4,8],
              [1,9,8,3,4,2,5,6,7],
              [8,5,9,7,6,1,4,2,3],
              [4,2,6,8,5,3,7,9],  # <---
              [7,1,3,9,2,4,8,5,6],
              [9,6,1,5,3,7,2,8,4],
              [2,8,7,4,1,9,6,3,5],
              [3,4,5,2,8,6,1,7,9]]

# check_sudoku should return True
valid = [[5,3,4,6,7,8,9,1,2],
         [6,7,2,1,9,5,3,4,8],
         [1,9,8,3,4,2,5,6,7],
         [8,5,9,7,6,1,4,2,3],
         [4,2,6,8,5,3,7,9,1],
         [7,1,3,9,2,4,8,5,6],
         [9,6,1,5,3,7,2,8,4],
         [2,8,7,4,1,9,6,3,5],
         [3,4,5,2,8,6,1,7,9]]

# check_sudoku should return False
invalid = [[5,3,4,6,7,8,9,1,2],
           [6,7,2,1,9,5,3,4,8],
           [1,9,8,3,8,2,5,6,7],
           [8,5,9,7,6,1,4,2,3],
           [4,2,6,8,5,3,7,9,1],
           [7,1,3,9,2,4,8,5,6],
           [9,6,1,5,3,7,2,8,4],
           [2,8,7,4,1,9,6,3,5],
           [3,4,5,2,8,6,1,7,9]]

# check_sudoku should return True
easy = [[2,9,0,0,0,0,0,7,0],
        [3,0,6,0,0,8,4,0,0],
        [8,0,0,0,4,0,0,0,2],
        [0,2,0,0,3,1,0,0,7],
        [0,0,0,0,8,0,0,0,0],
        [1,0,0,9,5,0,0,6,0],
        [7,0,0,0,9,0,0,0,1],
        [0,0,1,2,0,0,3,0,6],
        [0,3,0,0,0,0,0,5,9]]

# check_sudoku should return True
hard = [[1,0,0,0,0,7,0,9,0],
        [0,3,0,0,2,0,0,0,8],
        [0,0,9,6,0,0,5,0,0],
        [0,0,5,3,0,0,9,0,0],
        [0,1,0,0,8,0,0,0,2],
        [6,0,0,0,0,4,0,0,0],
        [3,0,0,0,0,0,0,1,0],
        [0,4,0,0,0,0,0,0,7],
        [0,0,7,0,0,0,3,0,0]]

def checkSanity(grid):
    """
    Returns a boolean depending on the sanity of the grid.
    Parameters
    ----------
    grid: the grid of which we chek validity (list)

    Returns
    -------
    sanity: true if grid is well-formed or False if ill-formed(bool)
    """
    sanity = True

    # Check that grid is a list of 9 lists
    if type(grid) is not list or len(grid) != 9:
        sanity = False
        return sanity

    # Loop on each element of grid
    for lines in grid:

        # Check that each element is a list
        if type(lines) is not list:
            sanity = False
            return sanity

        # Check that there are 9 elements in line
        if len(lines) != 9:
            sanity = False
            return sanity
 
        # Loop on each element of list
        for element in lines:
            # Check if element is invalid
            if 0 > element or 9 < element or type(element) is not int:
                sanity = False
                # Grid is ill-formed
                return sanity
    
    # Grid well-formed
    return sanity

def checkLine(line):
    """
    Returns a boolean depending on the validity of the line.
    Parameters
    ----------
    line: the line of which we're checking elements (list)

    Returns
    -------
    validity: true if line is valid, false otherwise (bool)
    """
    validity = True

    # Loop on elements of line
    for element in line:
        #Check if element is only once in the line
        if line.count(element) > 1 and element != 0:
            # element appears more than once so invalid
            validity = False
            return False

    return validity

def checkAllLines(grid):
    """
    Returns a boolean value depending on the validity of all lines.
    Parameters
    ----------
    grid: the grid of which we check the lines (list)

    Returns
    -------
    validity: true if all lines are valid (bool)
    """
    # Loop on all lines of grid
    for line in grid:
        if not checkLine(line):
            return False

    return True

def checkColumns(grid):
    """
    Returns a boolean value depending on the validity of all columns.
    Parameters
    ----------
    grid: the grid of which we check the columns (list)

    Returns
    -------
    validity: true if all columns are valid (bool)
    """
    validity = True

    # Loop on all column
    for colNum in range (0, 9):
        # Create a list which will contain the value of the column
        colList = []
        # Loop on each line of grid
        for line in grid:
            # Add number to list
            colList.append(line[colNum])
        
        # Check if column is valid
        if not checkLine(colList):
            validity = False
            return validity
    
    # If loop passed, then all columns are valid
    return validity

def getCaseList(grid, maxRowId, maxColId):
    """
    Returns a list containing the values of the corresponding case
    Parameters
    ----------
    grid: the grid in which are the cases (list)
    maxRowId:  number of last row of the case (int)
    maxColId: number of last column of the case (int)

    Returns
    -------
    caseList: list containing elements of the case (list)
    """
    # Initialize list of the case
    caseList = []

    # Loop on rows of case 
    for rowNum in range(maxRowId - 2, maxRowId + 1):
        # Loop on columns of case in each row
        for colNum in range(maxColId - 2, maxColId + 1):
            # Add number to list
            caseList.append(grid[rowNum][colNum])

    return caseList

def checkCases(grid):
    """
    Returns a boolean value depending on the validity of all cases.
    Parameters
    ----------
    grid: the grid of which we check the cases (list)

    Returns
    -------
    validity: true if all cases are valid (bool)
    """
    validity = True

    # Loop on each case
    for caseId in range(1,9):
        # Check in which case we are and define last row of each
        if caseId == 1 or caseId == 2 or caseId == 3:
            lastRow = 2
        elif caseId == 4 or caseId == 5 or caseId == 6:
            lastRow = 5
        elif caseId == 7 or caseId == 8 or caseId == 9:
            lastRow = 8

        # Check in which case we are and define last column of each
        if caseId == 1 or caseId == 4 or caseId == 7:
            lastCol = 2
        elif caseId == 2 or caseId == 5 or caseId == 8:
            lastCol = 5
        elif caseId == 3 or caseId == 6 or caseId == 9:
            lastCol = 8

        # Check if case is invalid
        if not checkLine(getCaseList(grid, lastRow, lastCol)):
            # case is invalid, return
            validity = False
            return validity
    
    return validity

def check_sudoku(grid):
    """
    Returns a boolean depending on the validity of the grid
    Parameters
    ----------
    grid: the grid of which we chek validity (list)

    Returns
    -------
    validity: true if grid is valid, false if it's not and none
    if it is ill formed. (bool)
    """
    # Initialize validity value
    validity = True

    # Check sanity of grid
    if not checkSanity(grid):
        # Grid ill-formed
        validity = None
        return validity

    # Grid is invalid (number appears more than once in line, columns or case)
    if not checkAllLines(grid) or not checkColumns(grid) or not checkCases(grid):
        validity = False
        return validity
    
    return validity

print (check_sudoku(ill_formed)) # --> None
print (check_sudoku(valid))   # --> True
print (check_sudoku(invalid))   # --> False
print (check_sudoku(easy))     # --> True
print (check_sudoku(hard))      # --> True

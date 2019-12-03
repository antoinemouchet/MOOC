# CHALLENGE PROBLEM: 
#
# Use your check_sudoku function as the basis for solve_sudoku(): a
# function that takes a partially-completed Sudoku grid and replaces
# each 0 cell with an integer in the range 1..9 in such a way that the
# final grid is valid.
#
# There are many ways to cleverly solve a partially-completed Sudoku
# puzzle, but a brute-force recursive solution with backtracking is a
# perfectly good option. The solver should return None for broken
# input, False for inputs that have no valid solutions, and a valid
# 9x9 Sudoku grid containing no 0 elements otherwise. In general, a
# partially-completed Sudoku grid does not have a unique solution. You
# should just return some member of the set of solutions.
#
# A solve_sudoku() in this style can be implemented in about 16 lines
# without making any particular effort to write concise code.

# solve_sudoku should return None
ill_formed = [[5,3,4,6,7,8,9,1,2],
              [6,7,2,1,9,5,3,4,8],
              [1,9,8,3,4,2,5,6,7],
              [8,5,9,7,6,1,4,2,3],
              [4,2,6,8,5,3,7,9],  # <---
              [7,1,3,9,2,4,8,5,6],
              [9,6,1,5,3,7,2,8,4],
              [2,8,7,4,1,9,6,3,5],
              [3,4,5,2,8,6,1,7,9]]

# solve_sudoku should return valid unchanged
valid = [[5,3,4,6,7,8,9,1,2],
         [6,7,2,1,9,5,3,4,8],
         [1,9,8,3,4,2,5,6,7],
         [8,5,9,7,6,1,4,2,3],
         [4,2,6,8,5,3,7,9,1],
         [7,1,3,9,2,4,8,5,6],
         [9,6,1,5,3,7,2,8,4],
         [2,8,7,4,1,9,6,3,5],
         [3,4,5,2,8,6,1,7,9]]

# solve_sudoku should return False
invalid = [[5,3,4,6,7,8,9,1,2],
           [6,7,2,1,9,5,3,4,8],
           [1,9,8,3,8,2,5,6,7],
           [8,5,9,7,6,1,4,2,3],
           [4,2,6,8,5,3,7,9,1],
           [7,1,3,9,2,4,8,5,6],
           [9,6,1,5,3,7,2,8,4],
           [2,8,7,4,1,9,6,3,5],
           [3,4,5,2,8,6,1,7,9]]

# solve_sudoku should return a 
# sudoku grid which passes a 
# sudoku checker. There may be
# multiple correct grids which 
# can be made from this starting 
# grid.
easy = [[2,9,0,0,0,0,0,7,0],
        [3,0,6,0,0,8,4,0,0],
        [8,0,0,0,4,0,0,0,2],
        [0,2,0,0,3,1,0,0,7],
        [0,0,0,0,8,0,0,0,0],
        [1,0,0,9,5,0,0,6,0],
        [7,0,0,0,9,0,0,0,1],
        [0,0,1,2,0,0,3,0,6],
        [0,3,0,0,0,0,0,5,9]]

# Note: this may timeout 
# in the Udacity IDE! Try running 
# it locally if you'd like to test 
# your solution with it.
# 
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
    grid: the grid of which we check validity (list)

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
            if 0 > element or 9 < element:
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

def checkValidity(grid):
    """
    Returns a boolean depending on the validity of the grid
    Parameters
    ----------
    Parameters
    ----------
    grid: the grid of which we check validity (list)

    Returns
    -------
    validity: true if grid is valid, false if it's not (bool)
    """
    validity = True

    # Grid is invalid (number appears more than once in line, columns or case)
    if not checkAllLines(grid) or not checkColumns(grid) or not checkCases(grid):
        validity = False
        return validity

    return validity

def check_sudoku(grid):
    """
    Returns a boolean depending on the validity of the grid
    Parameters
    ----------
    grid: the grid of which we check validity (list)

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
    if not checkValidity(grid):
        validity = False
        return validity
    
    return validity

def findNextHole(grid):
    """
    Returns emplacement of next unknown element in grid
    Parameters
    ----------
    grid: the grid we try to solve (list)

    Returns
    -------
    caseCoord: coordinates of case [row, column] (list)
    """
    # Initialize id of row at 0
    rowID = 0

    # Loop on rows in grid
    for row in grid:
        # Initialize id of column at 0
        colID = 0

        # Loop on elements of row
        for element in row:

            # If element is unknow return its coordinates
            if element == 0:
                return [rowID, colID]

            # Increase id of column
            colID += 1

        # Increase id of row
        rowID += 1

    return None

def displayGrid(grid):
    """
    Displays the sudoku grid
    Parameters
    ----------
    grid: the grid to display (list)

    """
    # Initialize variable to display
    display = ""

    # Initialize line counter
    lineID = 1
    # Loop on lines
    for line in grid:
        # Initialize column counter
        colID = 1
        # Loop on elements of line
        for element in line:
            # Don't add 0 to display
            if element != 0:
                # Add element to display
                display += str(element)
            
            else:
                display += " "
        
            # There is a separation between cases
            if colID % 3 == 0 and colID != 9:
                display += " | "

            # Go to next line
            elif colID == 9:
                display += "\n"

            # Space after any number
            else:
                display += " "
            
            # Increase id of column
            colID += 1

        # Lines 3 and 6 have a line after to separate cases
        if lineID % 3 == 0 and lineID != 9:
            display += "---------------------\n"
        # Increase id of line
        lineID += 1

    print(display)

def fill(grid):
    """
    Returns a boolean depending on if grid is complete and valid or not
    Parameters
    ----------
    grid: the grid we try to solve (list)

    Returns
    -------
    True if grid is full and valid, False otherwise (bool)
    """
    hole = findNextHole(grid)

    # Grid is complete and valid
    # That's the basic case of the recursion
    if hole == None:
        return True

    # Get line and row of next hole
    lineID = hole[0]
    elID = hole[1]

    # Define list of possible values.
    possibleValues = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Loop on possible values
    for value in possibleValues:

        # Update value in grid
        grid[lineID][elID] = value
        # Recursivity
        # If grid is valid, launch fill again
        if checkValidity(grid):
            #displayGrid(grid)
            # This should happen only when grid is full
            if fill(grid):
                return True
        
        # Reset value at position tested since it's invalid
        grid[lineID][elID] = 0

    # Go back
    # It gets here when grid is invalid
    return False

def solve_sudoku (grid):
    """
    Returns the solved grid when its valid, None when grid is ill-formed
    and False when grid can not be solved or is invalid
    Parameters
    ----------
    grid: the grid of which we check (list)

    Returns
    -------
    validity: true if grid is valid, false if it's not and none
    if it is ill formed. (bool)
    """

    # Check sanity of grid
    sanity = check_sudoku(grid)

    # Ill-formed grid
    if sanity == None:
        return None
 
    # Invalid grid
    elif sanity == False:
        return False

    # Valid grid 
    if fill(grid):
        return grid 

    # Impossible to solve grid
    return False

#displayGrid(solve_sudoku(easy))
#displayGrid(solve_sudoku(hard))
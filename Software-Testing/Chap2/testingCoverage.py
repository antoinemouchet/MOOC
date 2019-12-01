# SPECIFICATION:
#
# The stats function computes some basic statistics functions
# when given a list of numbers as input.
#
# TASK:
#
# Achieve full statement coverage on the stats function. 
# All you should have to do is modify the test function 
# to call stats with different lists of values.

def stats(lst):
    min = None
    max = None
    freq = {}
    # Loop on element of the list
    for i in lst:
        # Check if number is smaller than actual min (if there is one)
        if min is None or i < min:
            min = i

        # Check if number is greater than actual max (if there is one)
        if max is None or i > max:
            max = i
        # Check if number already appeared, if yes increase his nb of appearance by 1
        if i in freq:
            freq[i] += 1
        #Number didn't already appear, add into dict with nb appearance (value) at 1
        else:
            freq[i] = 1

    # Sort the list
    lst_sorted = sorted(lst)

    # Check if it's a list of even elements
    if len(lst_sorted)%2 == 0:
        # Get middle and median
        middle = len(lst_sorted)//2
        median = (lst_sorted[middle] + lst_sorted[middle-1]) / 2
    
    # List of odd elements
    else:
        median = lst_sorted[len(lst_sorted)//2]

    mode_times = None

    # Loop on frequence values
    for i in freq.values():
        # Check if it's the greatest amount of apparitions in dict
        if mode_times == None or i > mode_times:
            mode_times = i
    
    # Create a list
    mode = []
    # Loop on pairs item - value in dict
    for (num, count) in freq.items():
        if count == mode_times:
            mode.append (num)

    # Display infos
    print ("list = " + str(lst))
    print ("min = " + str(min))
    print ("max = " + str(max))
    print ("median = " + str(median))
    print ("mode(s) = " + str(mode))

def test():

    l = [31, 31]
    l2 = [35]
    stats(l)
    stats(l2)

test()

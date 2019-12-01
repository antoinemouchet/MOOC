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
        # BUG CREATED ON PURPOSE
        # Get absolute value of number
        i = abs(i)
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

# test1 should achieve full statement coverage of 
# the stats function without triggering the bug 
# you've inserted into the stats function.
def test1():
    ###Your test1 code here. Depending on what 
    # bug you choose to put in the stats function, 
    # you may or may not need to modify test1.
    l = [31, 31, 1, 2, 2, 1]
    stats(l)
    l = [31]
    stats(l)

# test2 should also achieve full statement coverage 
# of the stats function, but should trigger the bug 
# you've inserted into the stats function.
def test2():
    m =  [-42, -42, -59]
    n = [-56, -97]
    stats(m)
    stats(n)

test1()
test2()


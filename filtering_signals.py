# Sometimes it is necessary to filter a signal by frequency, e.g. to reduce 
# noise outside of the expected frequency range. Filters can be stacked, 
# allowing only the frequencies within the range allowed by all filters to 
# get through. For example, three filters with ranges of (10, 17), (13, 15) 
# and (13, 17) will only allow signals between 13 and 15 through. The only 
# range that all filters overlap is (13, 15). Given n signals frequencies and 
# a series of m filters that let through frequencies in the range x to y, 
# inclusive, determine the number of signals that will get through the 
# filters.

# For example given n = 5 signals with frequencies = [8, 15, 14, 16, 21] 
# and m = 3 filtersRanges = [[10, 17], [13, 15], [13, 17]], the 2 frequencies 
# that will pass through all filters are 15 and 14.

# Complete the 'countSignals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY frequencies
#  2. 2D_INTEGER_ARRAY filterRanges
#

def countSignals(frequencies, filterRanges):
    # iterate over filterRanges
    # check if each frequency fits in between those ranges
    # whichever one fits the least is the only one that works
    
    # first determine the lower and upper frequency bounds allowed
    range_min = None
    range_max = None
    for filterRange in filterRanges:
        if (range_min == None) or (filterRange[0] > range_min):
            range_min = filterRange[0]
        if (range_max == None) or (filterRange[1] < range_max):
            range_max = filterRange[1]
        
    # then count frequencies within lower and upper bounds
    count = 0
    for frequency in frequencies:
        # python's range(start, end) inclusive of start but not end, hence +1:
        if frequency in range(range_min, (range_max + 1)):
            count += 1
    
    return count

frequencies = [8, 15, 14, 16, 21]
filterRanges = [[10, 17], [13, 15], [13, 17]]

countSignals(frequencies, filterRanges)
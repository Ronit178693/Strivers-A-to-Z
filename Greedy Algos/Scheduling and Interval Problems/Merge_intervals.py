'''
Sort the given intervals on the basis of the starting points

if result is empty append the first interval in it or if the last intervals ending time is less then the next intervals starting time

If the starting time is < then the ending time of the previous interval then merge them 
'''

def merge(intervals):
    if (len(intervals) <= 1):
        return intervals
    intervals.sort(key = lambda intervals : intervals[0])
    result = []
    for i in intervals:
        # If result is not empty or the ending time of the last interval in the results is less then that of the new interval
        if (not result or result[-1][1] < i[0]):
            result.append(i)
        # There is an overlapping
        else:
            result[-1][1] = max(result[-1][1], i[1])
    return result
            
                
        
    
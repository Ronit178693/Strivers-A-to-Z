def insert(intervals, newInterval):
    # Break the intervals into 3 parts, 1) The left sorted part, 2) The Overlapping part, 3) The right sorted part 
    
    result = []
    i = 0
    # Checking for all the intervals which have their ending point less then the starting point point of the newInterval
    while( i < len(intervals) and intervals[i][1] < newInterval[0]):
        result.append(intervals[i])
        i += 1
    # This is the merging part 
    while(i < len(intervals) and intervals[i][0] <= newInterval[1]):
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    result.append(newInterval)
    while(i < len(intervals)):
        result.append(intervals[i])   
        i += 1     
    return result
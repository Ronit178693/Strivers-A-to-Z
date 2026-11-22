# To apply the greedy approach we will select the meetings with the smalles finishing time first, so that we can acomodate more meetings in the single room in the same time 
def n_meetings(start, end):
    intervals = []
    # As both start and end arrays will be of same length 
    for i in range(len(start)):
        # Forming the combined array
        intervals.append([start[i], end[i], i + 1])
    # Sorting the final array on he basis of ending time 
    intervals.sort(key = lambda intervals : intervals[1])
    order = []
    count, free_time = 0, 0
    for i in range(len(intervals)):
        if(intervals[i][0] >= free_time):
            count += 1
            free_time = intervals[i][1]
            order.append(intervals[i][2])
    return [order, count]
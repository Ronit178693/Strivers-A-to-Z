def divide(intervals):
    Max = 0
    for i in range(len(intervals)):
        count = 0
        for j in range(len(intervals)):
            # count every interval that is still running at the moment intervals[i] starts
            if(intervals[j][0] <= intervals[i][0] <= intervals[j][1]):
                count += 1
        Max = max(Max, count)
    return Max

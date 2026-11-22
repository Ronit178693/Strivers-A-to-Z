# Find the number of maximum not overlapping interval
    # subtract the length of the original list with the count to get the count of interval needed to be removed
def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        # Sort the array on the basis of ending time so select the meeting which ends early first, to maximize the number of intervals
        intervals.sort(key = lambda intervals : intervals[1])
        count, free_time = 0, float('-inf')
        for i in range(len(intervals)):
            if(intervals[i][0] >= free_time):
                count += 1
                free_time = intervals[i][1]
        return len(intervals) - count
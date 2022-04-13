def sum_of_intervals(intervals):
    expansion = [[i for i in range(interval[0], interval[1])]for interval in intervals]
    #put all values in one list
    length = list(set([item for sublist in expansion for item in sublist]))
    return len(length)
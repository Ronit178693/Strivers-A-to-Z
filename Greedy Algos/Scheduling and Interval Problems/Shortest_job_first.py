def sjf(processes):
    processes.sort()
    time, wt_time = 0, 0
    for i in range(len(processes)):
        
        
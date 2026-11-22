def Job_Sequencing(jobs):
    # Sorting the jobs in descending order on the basis of their profits 
    jobs.sort(key=lambda jobs : jobs[2], reverse = True)
    # This gives the maximum number of days needed to form the hash array
    max_deadline = float('-inf')
    for i in range(len(jobs)):
        if(jobs[i][1] > max_deadline):
            max_deadline = jobs[i][1]
            
            
    hash = [-1] * (max_deadline + 1)
    
    
    total_profit, count = 0, 0
    
    
    for i in range(len(jobs)):
        days_needed = jobs[i][1]
        id = jobs[i][0]
        profit = jobs[i][2]
        
        if(hash[days_needed] == -1):
            hash[days_needed] = id
            count += 1
            total_profit += profit
        else:
            while(days_needed > 0 and hash[days_needed] != -1):
                days_needed -= 1
            if(days_needed > 0):
                hash[days_needed] = id
                count += 1
                total_profit += profit
                
    return [total_profit, count]
                
                
        
def fractional_knapsack(items, w):
    # Sorting the items in the items list in descending order on the basis of value/weight ratio
    items.sort(key = lambda items : items[0]/items[1], reverse = True)
    total_profit = 0
    weight = w
    for i in range(len(items)):
        if(weight > 0):
            if(items[i][1] <= weight):
                # Adding the profit of the item to the knapsack
                total_profit += items[i][0]
                # reducing the capicity of the knapsack
                weight -= items[i][1]
            else:
                total_profit += (items[i][0]/items[i][1]) * weight 
                weight -= weight
                break
    return total_profit
        
    
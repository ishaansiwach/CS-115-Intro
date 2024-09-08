#Ishaan Siwach
#Professor Ryan
#I pledge my honor that I have abided by the Stevens Honor System

def knapsack(capacity, items):
    """This function returns the maximum value a knapsack can have for the
       maximum weight that the knapsack can hold. Each object in the knapsack
       has a specific weight and value."""
    if capacity==0:
        return 0
    if items==[]:
        return 0
    elif capacity<items[0][0]:
        return knapsack(capacity, items[1:])
    else:
        use=items[0][1]+knapsack(capacity-items[0][0],items[1:])
        lose=knapsack(capacity,items[1:])
        return max(use,lose)
    

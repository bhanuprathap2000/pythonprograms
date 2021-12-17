
def swap_without_temp(a,b):
    a=a+b
    b=a-b
    a=a-b
    
    #if we return multiple values then a tuple of values will be returned
    return a,b
    
print(swap_without_temp(5,10))

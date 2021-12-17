
def factorial(number):
    
    #this is a base case to return 1
    if number<=1:
        return 1
    #this is a recurrsive case
    return number*factorial(number-1)
print(factorial(5))

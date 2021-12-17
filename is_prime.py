
def is_prime(number):
    
    """
    
    check the divisibility by all numbers between 2 and (number-1)
    if divisible by any number
    then return False and break
    
    if not check all the numbers in the range of number-1 and 2
    and  if number is not divisible by any numbers in that range then else for loop will run and return True
    
    """
    
    for i in range(2,number-1):
        if number%i==0:
            return False
            break
    else:
        return True
        

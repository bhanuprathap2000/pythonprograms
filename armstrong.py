
def is_arm_strong(number):
    """
    Given a number is said to be arm strong if
    
    abcd... = a^n + b^n + c^n + d^n + ...
    
    here n is length of the number
    
    The logic to solve is that get the individual digit and raise them to power of length
    and add them all.
    
    if sum of the individual digits is equal to the number passed then we can all it armstrong.
    
    
    """
    
    sum=0#this variable contains the sum of individual digits raised to power of length.
    temp=number# this variable is temp variable which we reduce the digits
    while temp>0:
        digit=temp%10#in order to a digit
        sum=sum+digit**len(str(number))#this will perform the sum
        temp=temp//10 /#this will remove the last digit
    
    if sum==number:
        return True
    else:
        return False

print(is_arm_strong(407))
        

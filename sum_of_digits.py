
def sum_of_digits(number):
    
    sum=0
    
    temp=number
    
    """
    get the last digit
    add sum =sum+digit
    
    """
    
    while temp>0:
        digit=temp%10
        sum=sum+digit
        temp=temp//10
    return sum

print(sum_of_digits(11))


# reverse a number

def reverse_number(number):
    
    """
    in order to reverse_number we need to get the last digit
    then 
    reverse= reverse*10 +digit
    
    """
    
    temp=number#we need to store the temp
    reverse=0
    while temp>0:
        digit=temp%10
        #this particular statement is making sure that we also keep the position in mind
        reverse= reverse*10 +digit
        temp=temp//10
    return reverse
        
print(reverse_number(15))


def reverse_string(string):
    
    """
    reverse a string using the for loop
    """
    reverse=""
    for i in string:
        reverse=i+reverse
    return reverse
    
print(reverse_string("bhanu"))
    


def is_palindrome_string(string):
    
    #the string doesn't support the built in reverse method 
    #so we need to reverse them manually
    reverse_string=""

    for i in string:
        #this is used to reverse
        reverse_string=i+reverse_string
        
        
    
    if (reverse_string==string):
        return True
    else:
        return False
        
print(is_palindrome_string("bhanu"))

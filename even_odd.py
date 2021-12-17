
def is_even_odd(number):
    
    #we perform a bitwise and with 1 and number if result 0 then even or Odd
    #this is because the odd numbers have last digit 1 and even digit 0
    if (number & 1)==0:
        return "Even"
    else:
        return "Odd"
        
print(is_even_odd(4))

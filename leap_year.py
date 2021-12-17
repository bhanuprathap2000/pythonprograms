def is_leap_year(year):
    
    """
    logic is 
    
    if year not  divisible by 4 then it is not prime
    if year divisible by 4 then check divisible by 100 if not divisible by 100 then it is a leap year.
    if divisible by 400 then it is leap year else not leap year
    
    """


    if year%4==0:
        
        if year%100==0:
            
            if year%400==0:
                return True
            else:
                return False
        return True
    
    else:
        return False
        
print(is_leap_year(2004))
print(is_leap_year(2005))

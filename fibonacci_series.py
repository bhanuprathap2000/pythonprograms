#using recurssion
def fibonacci_series(n):
    #this is a base case to exit
   if n <= 1:
       return n
    #this is a recurssive case
   else:
       return(fibonacci_series(n-1) + fibonacci_series(n-2))
       
for i in range(5):
    print(fibonacci_series(i))
    
#using the for loop


def fibonacci_series(number):
    
    """
    Given any number it returns the fibonacci_series of those many terms
    
    """
    
    t1=0
    t2=1
    
    print(t1,t2,end=" ")
    
    count=2
    
    while count<number:
        t3=t2+t1
        print(t3,end=" ")
        t1=t2
        t2=t3
        count=count+1
        
fibonacci_series(5)


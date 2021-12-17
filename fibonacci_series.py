
def fibonacci_series(n):
    #this is a base case to exit
   if n <= 1:
       return n
    
   else:
       return(fibonacci_series(n-1) + fibonacci_series(n-2))
       
for i in range(5):
    print(fibonacci_series(i))

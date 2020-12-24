# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 15:32:31 2020

@author: Bhanu
"""
import numpy as np
gradesnum=[10,9,8,7,6,5,4]
print("Welcome to the SGPA Calculator")
totalsubjects=int(input("Enter the number of subjects In the semester\n"))
student_details_grades=[]
student_details_credit=[]


print("Please enter the grades properly accepted are:")
print(f"{gradesnum} ")
count=0

while (count<totalsubjects):
    subject=int(input("Enter the grade\n"))
    credit=int(input("Enter the credit for that subject\n"))
    student_details_grades.append(subject)
    student_details_credit.append(credit)
    count+=1



    
        

def sgpa_calculate():
    numerator=0
    denominator=0
    grade=np.array(student_details_grades)
    credit=np.array(student_details_credit)
    numerator=grade*credit
    nume=numerator.sum()
    denominator=credit.sum()
    sgpa=nume/denominator
    print(f"Your SGPA is {sgpa}.")
    
sgpa_calculate()

    

        
            
    
    


    


# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 13:40:56 2020

@author: Bhanu
"""
def highest_bidder():
    highest=0
    highestbidder=""
    for bidder in bidder_details:
        bidamount=bidder_details[bidder]
        if bidamount>highest:
            highest=bidamount
            highestbidder=bidder
            
    print(f"The highest bidder is {highestbidder} and the bid amount is {highest} ruppes")
    
bidder_details={}

more=True
while more:
    name=input("Enter your name\n")
    bid_amount=int(input("Enter the bid amount in ruppes\n"))
    bidder_details[name]=bid_amount
    more_bids=input("Tap yes for any other bids else no\n").lower()
    if more_bids=="no":
        more=False
        highest_bidder()

    

            
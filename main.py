from art import logo
import os 
clear=lambda:os.system('cls')

print(logo)
bid={}
bidStatus="True"
winner=""


def highestBid(bid):
    highest_bid=0
    for bidder in bid:
        bid_amount=bid[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f"The Winner is {winner} with bid of ${highest_bid}")


while bidStatus:
    name=input("What is your name? \n")
    price=int(input("What is your bid?\n$"))
    bid[name]=price
    shouldContinue=input("Are there any other bidders? Type 'Yes' or 'No' ?")
    if shouldContinue =="no" or shouldContinue =="NO" or shouldContinue =="No":
        bidStatus=False
        highestBid(bid)
    elif shouldContinue =="yes" or shouldContinue =="YES" or shouldContinue =="Yes":
        clear()
    


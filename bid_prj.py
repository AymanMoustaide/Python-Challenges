from os import system, name
 
# import sleep to show output for some time period
from time import sleep

# define our clear function
def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

#_HIGHER BIDDER NEW PRJ



bids = {}
bidding_finished = False

def find_highest_bidder(bids):
    highest_bid = 0
    winner = ''
    # bidding_record = bids
    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is, {winner} with a bid of ${highest_bid}")

while not bidding_finished:

    name = input ("What is your name?")
    price = int(input ("What is your bid? $"))
    bids [name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
        
    elif should_continue == 'yes':
        continue



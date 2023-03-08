
def find_highest_bidder(bidding_record):
    high_bid = 0
    for name, bid in bids.items():
        if bid > high_bid:
            high_bid = bid
        if bid == high_bid:
            print(f"{name} wins with a high bid of ${high_bid}")


print("Blind Auction")
bids = {}
flag = True
while flag:
    name = input("Please enter your name: ")
    bid = float(input("Please enter your bid: "))
    bids[name] = bid
    more_bids = input("Are there more bids? yes/no ")
    if more_bids == 'no':
        flag = False 

find_highest_bidder(bids)


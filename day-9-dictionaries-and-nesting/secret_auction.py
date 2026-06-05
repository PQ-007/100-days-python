print('''                ___________
                                   /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| -' ' '---------'' '-'
                          )"""""""(
                         /_________\
                       .-------------.
                      /_______________\ ''')

print("Welcome to the secret auction program.")

bids = {}

while True:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bids[name] = bid
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if more_bidders == "no":
        break
    print("\n" * 100)

highest_bid = 0
winner = ""
for bidder in bids:
    if bids[bidder] > highest_bid:
        highest_bid = bids[bidder]
        winner = bidder
print(f"The winner is {winner} with a bid of ${highest_bid}.") 

    



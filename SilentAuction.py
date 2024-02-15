"""The task is to design and write a program which takes care of a silent
auction. The program should start off by asking for the bidding item, and the
reserve price, which is requested from the auction manager before the auction
starts. It should then repeatedly: show the highest bid so far, ask for a bid,
and check if the bid placed is higher than the highest bid so far. If it is a
higher bid, store the bid. Otherwise, show a “need a higher bid” message. The
program needs a way of being terminated by the user. Build in some prearranged
signal value (e.g. a bid of -1) to end the loop on demand. When the user stops
the input loop, the highest bid should be checked to see if it beat the
reserve. If the reserve price is met, the highest bid should be displayed. If
not, a message saying the object didn't sell should be displayed.
"""


def answer_checker(question):
    error = "\nYou must enter a valid item\n"
    item = ""
    while not item:
        try:
            item = str(input(question))
            return item
        except ValueError:
            print(error)


def number_checker(question):
    error = "\nYou must enter a valid price\n"
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print(error)


def highest_bid():
    highest_bid = 0
    


# Main Routine
AUCTIONED_ITEM = answer_checker("What is the auction for: ")
print(AUCTIONED_ITEM)
RESERVE_PRICE = number_checker("What is the reserve price")
print()
print(f"The auction for the {AUCTIONED_ITEM} has started!")
highest_bid()
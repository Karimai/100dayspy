from replit import clear
from art import logo

class Auction:
    
    def __init__(self):
        self.bidders = []
        
    def add_bidder(self, name, amount):
        bidder = {"name": name, "bid": amount}
        self.bidders.append(bidder)
    
    def get_highest_biddder(self):
        highest_bidder = max(self.bidders, key=lambda bidder: bidder["bid"])
        return highest_bidder
    
    def start_auction(self):
        print(logo)
        print("Welcome to the private bidding auction.")
        auction_ongoing = True
        
        while auction_ongoing:
            name = input("What is your name?")
            try:
                bid = float(input("How much would you like to bid? : $"))
            except Exception as e:
                print("Please enter a valid float number!")
                continue
            self.add_bidder(name, bid)
            
            others = input("Are there any other bidder? (y/n)")
            if others.lower().startswith("n"):
                auction_ongoing = False
                highest_bidder = self.get_highest_biddder()
                print(f"The highest bidder is {highest_bidder['name']} with a ${highest_bidder['bid']:.2f}")
                print("Thanks for your participation")
            else:
                clear()
                
auction = Auction()
auction.start_auction()

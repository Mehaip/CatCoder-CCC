class Auction:

    def __init__(self, current_price, bidder_input, bid_input):
        self.bidder_input = bidder_input
        self.bid_input = bid_input
        self.current_price = current_price
        self.bidders = set(self.bidder_input)

    maximum_bid = 0
    highest_bidder = ""

    def maximum_bid_and_bidder(self):

        self.bidder_input.reverse()
        self.bid_input.reverse()
        for bidder in self.bidders:
            bidder_position = self.bidder_input.index(bidder)
            if int(bid_input[bidder_position]) > int(self.maximum_bid):
                self.highest_bidder = bidder
                self.maximum_bid = int(bid_input[bidder_position])

        print(f"{self.highest_bidder},{self.maximum_bid}")




        









if __name__ ==  "__main__":

    while True:
        bidding_input = input(">>>")
        current_price = bidding_input[0]
        current_price = int(current_price)
        bidding_input = bidding_input[2:].split(',')
        bider_input = []
        bid_input = []

        for index in range(0, len(bidding_input)):
            if index % 2 == 0:
                bider_input.append(bidding_input[index])
            else:
                bid_input.append(bidding_input[index])

        a = Auction(current_price, bider_input, bid_input)
        a.maximum_bid_and_bidder()







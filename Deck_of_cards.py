class Card(object):
    def __init__(self,suit,val,number):
        self.suit = suit
        self.val= val
        self.number= 0


    def yourTypes(self):
        print "Your suit is: ", self.suit
        return self

    def yourSelect(self):
        print "Your value is: ", self.val
        return self

    def yourCount(self):
        print "You recieved", self.number, "cards."
        return self

new_card = Card('heart', '10', 2)
new_card.yourTypes().yourSelect().yourCount()
#
# class Deck(object):
#     def __init__ (self):
#         super(card,self), __init__()
#         self.deckTotal = 52
#         self.suitTotal = 4
#         self.valueTotal = 13
#
#     def dealTwo(self):

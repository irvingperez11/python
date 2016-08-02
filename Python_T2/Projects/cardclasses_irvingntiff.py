
import random

class Card(object):

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        if self.rank != "10":
            card = """
            __________
            |        |
            |   """+self.rank+"""    |
            |  """+self.suit+""" |
            |        |
            |________|"""
            return card
        else:
            card = """
            __________
            |        |
            |  """+self.rank+"""    |
            |  """+self.suit+""" |
            |        |
            |________|"""
            return card

class Deck(object):
    
    def __init__(self):
        suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
        rank_names = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        
        self.cards = []
        for suit in suit_names:
            for rank in rank_names:
                card = Card(suit,rank)
                self.cards.append(card)
                           

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
       
        self.cards.remove(card)


    def shuffle(self):
       
        random.shuffle(self.cards)


deck = Deck()

for card in deck.cards:
    print card


#I see thou is trying hard

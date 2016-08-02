import random
class Card(object):
    def __init__(self, char, suit):
        self.char = char
        self.suit = suit
    def __str__(self):
        if self.char != "10":
            card = """
            _________
            |        |
            |   """+self.char+"""    |
            |  """+self.suit+""" |
            |        |
            |________|"""
            return card
        else:
            card = """
            __________
            |        |
            |  """+self.char+"""    |
            |  """+self.suit+""" |
            |        |
            |________|"""
            return card
            
class Player(object):
    def __init__ (self,name):
        self.name = name
        self.hand = []
        self.hand_index = []
        self.count = len(self.hand)
    def add_card(self,card):
        self.hand.append(card)

    def remove_card(self,card):
        
        self.hand.remove(card)
        
        
class Deck(object):
    def __init__(self,suits,char):
        self.suits = suits
        self.char = char
        self.cards = []
        
        for suit in self.suits:
            for number in self.char:
                new_card = Card(str(number),suit)
                self.cards.append(new_card)
    def deal_hand(self,player):
        total = 4
        while total != 0:
            nums = random.randint(0,len(self.char) - 1)
            player.hand_index.append(nums)
            player.hand.append(self.cards[nums])
            self.cards.remove(self.cards[nums])
            total = total - 1
    def print_hand(self,player):
        print player.name
        for card in player.hand:
            print card
    def deal_cards(self,person,num):
        t = num
        while t != 0:
            person.hand.append(self.cards[random.randint(0,len(self.cards) - 1)])
            t -= 1

    def shuffle(self):
       
        random.shuffle(self.cards)

class Players(object):
    def __init__(self,name):
        self.name = name
        self.hand = []
        self.card_count = len(self.hand)
    
    def remove_card(self,card):
        self.hand.remove(card)
    
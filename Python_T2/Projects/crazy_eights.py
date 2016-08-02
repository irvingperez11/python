from cardclasses.irvingandtiffany import *

deck = Deck() #makes a deck object

player = Player("Irving") #makes the player object
opponent = Player("Tiffany") #Enemy
deck.deal_cards(player) #this deals the card to the player class so that s/he has cards
deck.deal_cards(opponent)

def print_hand(player):
    
    for card in player.hand:
        print  card

#Print the cards to show hand
gameplay = True
top_card = random.choice(deck.cards)

while gameplay:
    print "         Current top card"
    print top_card
    print "         _________________________"
    myturn = True
    while myturn:
        print player.name +"'s hand."
        print_hand(player)
        play = int(raw_input("What card shall you play? What number card?")) - 1
        playing_card = player.hand[play]
        if playing_card.suit == top_card.suit or playing_card.rank == top_card.rank:
            top_card = playing_card
            player.remove_card(playing_card)
        else:
            print "That card is not a valid play. You pass."
            player.hand.append(deck.cards[random.randint(0,len(deck.cards) - 1)])

        myturn = False
        #Enemy's turn
    while not myturn:
        print opponent.name,"has",opponent.card_count,"left"
        find_card = False
        while not find_card:
            for card in opponent.hand:
                if card.suit == top_card.suit or card.rank == top_card.rank:
                    find_card = True
                    top_card = card
                    print "The computer plays",card
                    opponent.remove_card(card)
                    break
                    
            if not find_card:
                print opponent.name + " cannot play. " + opponent.name +" passes."
                opponent.hand.append(deck.cards[random.randint(0,len(deck.cards) - 1)])
                myturn = True
                find_card = True #even though it is not
        myturn = True
                    
    
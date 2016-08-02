from card_player_classes_StephanRichard import *


players = Player("Irving") #makes the player object
opponent = Player("Tiffany") #Enemy
deck.deal_cards(players) #this deals the card to the player class so that s/he has cards
deck.deal_cards(opponent)

def print_hand(players):
    
    for card in players.hand:
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
        print players.name +"'s hand."
        print_hand(players)
        play = int(raw_input("What card shall you play? What number card?")) - 1
        playing_card = players.hand[play]
        if playing_card.char == top_card.char or playing_card.char == top_card.char:
            top_card = playing_card
            players.remove_card(playing_card)
        else:
            print "That card is not a valid play. You pass."
            players.hand.append(deck.cards[random.randint(0,len(deck.cards) - 1)])

        myturn = False
        #Enemy's turn
    while not myturn:
        print opponent.name,"has"
        find_card = False
        while not find_card:
            for card in opponent.hand:
                if card.char == top_card.char or card.char == top_card.char:
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
                    
    
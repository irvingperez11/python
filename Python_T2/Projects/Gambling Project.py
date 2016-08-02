import random
def Dice():
        die1 = random.randrange(1,7)
        die2 = random.randrange(1,7)
        sum = die1 + die2
        print "Player rolled", die1, "+", die2, "=", sum
        return sum
       
score = Dice()
 
if score == 7 or score == 11:
        game = "WON"
elif score == 2 or score == 3 or score == 12:
        game = "LOST"
else:
        game = "CONTINUE"
        points = score
        print "Point is", points
       
while game == "CONTINUE":
        sum = Dice()
        if sum == points:
                game = "WON"
        elif sum == 7:
                game = "LOST"
if game == "WON":
       print "Player wins"
else:
     print "Player loses"
       

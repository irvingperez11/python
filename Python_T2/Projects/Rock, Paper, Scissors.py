import random 

print "Hi get ready to play Rock, Paper, Scissors(Martin this is the order)"
print "\n" #This adds a space 
print "Please select: " 
print "1  Rock" 
print "2  Paper" 
print "3  Scissors" 

player = input ("Choose from 1-3: ") 

if player == 1: 
    print "You choose Rock" 
    print "CPU chooses Paper" 
    print "You lose!" 

elif player == 2: 
    print "You choose Paper" 
    print "CPU chooses Scissors" 
    print "You lose!" 

elif player == 3: 
    print "You choose Scissors" 
    print "CPU chooses Rock" 
    print "You lose!"

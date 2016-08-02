word = "cookie"
guess = raw_input("Guess a letter: ")
rguess =''
Nwrong = 0
foundword = False
while (Nwrong < 6) or (foundword):
#Checks for the guessed letter in the word then prints dashes for missing letter and prints the correct letter
    if guess in word:
        print guess
        
        guess = raw_input("Guess a letter: ")
    else:
        print 'Not a letter guess again'
        Nwrong +=1
        guess = raw_input("Guess a letter: ")
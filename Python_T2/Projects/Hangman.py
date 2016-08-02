word = "cookie"
guess = raw_input("Guess a letter: ")
print guess


Nwrong = 0
foundword = False

while (Nwrong == 6) or (foundword):
    if guess == word[0]:
        print guess
    else:
        Nwrong += 1
        print Nwrong
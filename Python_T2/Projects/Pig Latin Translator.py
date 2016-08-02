"""def piglatin():
    word = raw_input("Enter a word: ")
    new = word[:1] + word[:0] + 'ay'
print word"""
"""z = str(raw_input("Enter a phrase or word: ")).split()
def pig(z):
     x =  z[1:] + z[0] + 'ay'
     print x
pig(z)"""
    
    
def main():
    words = str(input("Input Sentence:")).split()
    for word in words:
            print(word[1:] + word[0] + "ay", end = " ")
    print ()

main()
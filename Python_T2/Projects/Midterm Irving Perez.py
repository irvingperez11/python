
#mission = "To educate responsible citizen-scholars for success in the college of their choice and a life of active citizenship"
mission = raw_input("Enter a sentence: ")

vowels = {'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U':0}
cons = { }
for letter in mission:
    uppercase_letter = letter.upper()
    if uppercase_letter in vowels:
        vowels[uppercase_letter] = vowels[uppercase_letter] + 1
        print vowels
    else:
        if uppercase_letter not in cons:
            cons[uppercase_letter] = 1
        else:
            cons[uppercase_letter] += 1
            
print cons
    
for letter in vowels:
    print  letter,'|', ('*' * vowels[letter]) 

for letter in cons:
    print letter,'|', ('*' * cons[letter])
"""
A = 0
E = 0
I = 0
O = 0
U = 0

for letter in mission:
    
    if letter == 'a':
        A += 1
    if letter == 'e':
        E += 1
    if letter == 'i':
        I += 1
    if letter == 'o':
        O += 1
    if letter == 'u':
        U += 1    

print 'A|', ('*' * A) 
print 'E|', ('*' * E)
print 'I|', ('*' * I)
print 'O|', ('*' * O)
print 'U|', ('*' * U)"""
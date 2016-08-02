dnumber = raw_input("Enter a Decimal Number: ")

n = 0

# checking if the decimaimal is in the string
for number in dnumber:
    if number == ".":
        print "Found Decimal"
        break   
    n = n + 1
    
# n = 1    
hundreths = int(dnumber[n + 2])

if hundreths >= 5: 
    #round up
else:
    #Truncate
number = raw_input("What number: ")
print number
n = len (number)
print n 

for number in xrange(n):
    if number%2==0:
        print "Even"
    else:
        print "odd"
   
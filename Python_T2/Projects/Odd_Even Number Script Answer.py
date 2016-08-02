print "Hello person"
number = raw_input("What number: ")
print number
n = len (number)
print n 

# varible to store information about number or not
all_numerical = True

for x in xrange(n):
    print "Loop", x
    if number[x] in ['0','1','2','3','4','5','6','7','8','9']:
        print number[x], "Is a number"
    else:
        print number[x], "Is NOT a number"
        all_numerical = False 
        

if all_numerical:
    print number,"Looks like you are smart", number,"is a number"
    my_int = int(number)
    if my_int%2==0:
        print "This is an even number"
    else:
        print " This is an odd number"
else:
    print number,"Yo stupid!!!", number,"isn't a number."





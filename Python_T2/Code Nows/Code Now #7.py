import time
my_str = raw_input("Enter a password: ")

char = len(my_str)

my_str = my_str.replace('a' ,'@').replace('e','3').replace('i', '1').replace('o','0').replace('u','2').replace('A' ,'@').replace('E','3').replace('I', '1').replace('O','0').replace('U','2').replace(' ' ,'_')

print "Calculating Password please wait"

time.sleep(3)


if char >= 8:
    print my_str
    
if char < 8:
    print "Has to be longer than 7 characters"
    
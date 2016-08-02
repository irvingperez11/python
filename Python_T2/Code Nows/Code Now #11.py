myFile = open('data.txt','r')


total = 0.0

for line in myFile:
    print total 

    total = total + float(line.replace('\n',''))
average = total/15


print "You're total is", total
print "You're average is", average
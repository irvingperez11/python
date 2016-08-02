fname = open("Essay.txt",'r')

num_words = 0 
num_char = 0

for line in fname:
    words = line.split()
    num_words += len(words)
    num_char += len(line)

print "Your word count is", num_words
print "Your character count is", num_char

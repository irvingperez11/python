poem = open("road.txt",'r+')


print poem.read().replace('and','but').replace('in','by').replace('And','But').replace('I','Irving')    

rword = {'I':'Irving','And':'But','and':'but','in':'by'}

for words in poem:

    if words == 'I':
        poem.split().replace('I','Irving')

    if words == 'And':
        poem.split().replace('And','But')
    
    if words == 'and':
        poem.split().replace('and','but')
    
    if words == 'in':
        poem.split().replace('in','by')
    
print poem.read().replace('and','but').replace('in','by').replace('And','But').replace('I','Irving')    

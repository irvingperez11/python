import getpass
import time

mes = getpass.getpass("Send a Message: ")
erepo = raw_input("would you like to encode your message y/n: ")
#raw_input("Send a Message: ")
emes = ''

alph = {'A':'B','a':'b','B':'V','b':'v','C':'G','c':'g','D':'Q','d':'q','E':'K','e':'k','F':'M','f':'m','G':'N','g':'n','H':'A','h':'a','I':'D','i':'d','J':'Z','j':'z','K':'C','k':'c','L':'W','l':'w','M':'S','m':'s','N':'E','n':'e','O':'O','o':'o','P':'Y','p':'y','Q':'F','q':'f','R':'J','r':'j','S':'X','s':'x','T':'H','t':'h','U':'T','u':'t','V':'L','v':'l','W':'P','w':'p','X':'V','x':'v','Y':'I','y':'i','Z':'R','z':'r',' ':' '}

inv_alph = {v:k for k, v in alph.items()}
if erepo == "y":
    print "Encoding Message..."
    time.sleep(2)
    for letter in mes:
         emes += alph[letter]
elif erepo == "Y":
    print "Encoding Message..."
    time.sleep(2)
    for letter in mes:
         emes += alph[letter]
elif erepo == "n":
    time.sleep(2)
    print "Fine werido here is your orginal message"
    print mes
elif erepo == "N":
    time.sleep(2)
    print "Fine werido here is your orginal message"
    print mes
else:
    print "What are you stupid?"
     
print emes

memes = ''

repo = raw_input("Decode Message y/n: ") 

if repo == "y":
    print "Decoding Message..."
    time.sleep(2)
    for letter in emes:
        memes += inv_alph[letter]

elif repo == "Y":
    print "Decoding Message..."
    time.sleep(2)
    for letter in emes:
        memes += inv_alph[letter]

elif repo == "N":
    time.sleep(1)
    print "Fine I'll keep it a secret"

elif repo == "n":
    time.sleep(1)
    print "Fine I'll keep it a secret"

else:
    print "Not a valid response. So Stupid"

print memes
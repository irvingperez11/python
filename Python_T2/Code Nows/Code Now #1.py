# # My code 
# words = ['bright','sensor','callous','despondent','judge','Martin','fallen','contrite','fetid']

# vowels = ['a','e','i','o','u']

# for word in words:
#     if vowels[] in word:
#         print word
#         # TODO: write code...

#Martins code
words = ['bright','sensor','callous','despondent','judge','Martin','fallen','contrite','fetid']

for word in words:
   nVowels = 0
   for letter in word:
      if letter in ['a','e','i','o','u']:
         nVowels = nVowels + 1
   if nVowels == 2:
         print word, "has exactly two vowels"
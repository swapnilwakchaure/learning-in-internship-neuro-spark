# Additional Regex Syntax

import re

regex1 = re.search(r'cat', 'The cat is here.')
# findall gives the array of word that we find
regex2 = re.findall(r'at', 'The cat in the hat sat there.')
# if we want to take the whole word that contains finding input
regex3 = re.findall(r'..at', 'The cat in the hat splat there.')
# it contains starts with (^) and end with ($) sign to search the given input at start and end
regex4 = re.findall(r'^\d', '2 is the number')
# end with
regex5 = re.findall(r'\d$', 'The number is 2')
# if we want to find anywhere then
regex6 = re.findall(r'\d', 'The number 2 is a prime number.')
# print('regex1: ', regex1) # <re.Match object; span=(4, 7), match='cat'>
# print('regex2: ', regex2) # ['at', 'at', 'at']
# print('regex3: ', regex3) # [' cat', ' hat', 'plat']
# print('regex4: ', regex4) #
# print('regex5: ', regex5) #
# print('regex6: ', regex6) #



# remove the numbers from the sentence
phrase = 'There are 3 numbers 34 inside 5 this sentence.'
pattern = r'[^\d]+'
regex7 = re.findall(pattern, phrase)
print(regex7) # ['There are ', ' numbers ', ' inside ', ' this sentence.']


# we can also remove punctuation marks using regex
test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
regex8 = re.findall(r'[^!.? ]+', test_phrase)
print(regex8) # ['This', 'is', 'a', 'string', 'But', 'it', 'has', 'punctuation', 'How', 'can', 'we', 'remove', 'it']
# join a sentence without punctuation
regex9 = ' '.join(regex8)
print(regex9) # This is a string But it has punctuation How can we remove it


# get the two words which add together with using hypen(-)
text = 'Only find the hypen-words in this sentence. But you do not know how long-ish they are.'
regex10 = re.findall(r'[\w]+-[\w]+', text)
print(regex10) # ['hypen-words', 'long-ish']


# get the combine words
textone = 'Hello, would you like some catfish?'
texttwo = 'Hello, would you like to take a catnap?'
texthree = 'Hello, have you seen this caterpillar?'
regex11 = re.search(r'cat(fish|nap|erpillar)', textone)
print(regex11) # <re.Match object; span=(27, 34), match='catfish'>
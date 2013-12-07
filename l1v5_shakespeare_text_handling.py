# Notes from Berkely CS61A FA2013
# credit to John DeNero's online course videos
# http://www-inst.eecs.berkeley.edu/~cs61a/fa13/
# http://www.youtube.com/user/papajohnno

from urllib.request import urlopen

# open shakespeare file

# open local version
shakes = open('shakespeare.txt')

# or web open
# shakes = urlopen('http://composingprograms.com/shakespeare.txt')

text = shakes.read().split()

#first 25 words
print(text[:25])

#len of text
print("Length of shakespeare.txt:", len(text))

#count number of the
print('Number of occurances of "the":', text.count('the'))

#put all the words into a set.  In a set, word only occur once
words = set(text)

#number of unique words
print('Number of unique words:', len(words))

print('The max word: ',max(words))

#the max word backwards
print('The max word backwards: ', max(words)[::-1])

#reverse a string
print('Longest word:',max(words, key=len))

#find all words over 4 letters spelled the same when reversed
print({w for w in words if w == w[::-1] and len(w) > 4})

#find all 4 letter words that spelled backwards is
#another word in the list
print({w for w in words if w[::-1] in words and len(w) == 4})







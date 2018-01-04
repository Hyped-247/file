# this program will take file and will do the following.
# the function wordcount: it will count the number of words. including he's
# the  function percet: will count the number of words that will count as 1%. ex. if there is 100 words, then for it to count it  must appear at least once.  it makes a difference when there is a large number of words.
# the function word_filter: is putting all the words in a list( including he's), then checking  if they count as one percent or more then  the program will print it out.
# by Mo..
#  http://stackoverflow.com/questions/2600191/how-can-i-count-the-occurrences-of-a-list-item-in-python

from math import *
from collections import Counter

def wordcount(filename): # this will count the number of words.
	look = open(filename, "r")
	careful_look = look.readlines()
	look.close()
	words_count = 0
	for each in careful_look:
		word_check = each.split()
		for word in word_check:
			word = word.lower()
			word = word.strip("!@#$%^&*()_+-+=][{}|\\':;><,.?/~`=...---___-—")
			word = word.replace('\'', '')
			if True == word.isalpha():
				words_count += 1
	return words_count

def percet(filename): # this will tell you how many times a word need to  occur to be more than 1%
	amount = wordcount(filename)
	amount = amount * 0.01
	amount = ceil(amount)
	return amount


def word_filter(filename):
	try:
		amount = wordcount(filename) # this is the number of words
		limit = percet(filename) # this is how many words you need for it to be more than 1%
		look = open(filename, "r") # opne the file
		careful_look = look.readlines() # read the file.
		look.close() # close the close
		wordfreq = [] # create an empty list that will put all the word in it
		for each in careful_look: # each:  will be  represent each line.
			word_check = each.split() # now it will become a list
			for x in word_check: # x:  will be each word in the line
				x = x.lower() # make sure that x is lowercase
				x = x.strip("!@#$%^&*()_+-+=][{}|\\':;><,.?/~`=...---___-—") # take punctuation out.
				x = x.replace('\'', '') #delete comments that are in middle of a string. ex. he's will become hes.
				if True == x.isalpha(): # make sure that x is an  alphabetical letter.
					wordfreq.append(x) # if it is an alphabetical word add it to the list.
		cool = Counter(wordfreq) # this will  convert the list wodfreq to a  Dictionary.
		# the key's will be the word. And the vaules will be how many time it  occurred.
		for k, v in cool.items(): # this will loop through the  Dictionary.
			if v > limit: # this will check if the word occurred more than 1%.
				# check line 30 if you don't know what limit is.
				print(k,":", v)
	except FileNotFoundError: # this will make sure that the file  exist.
			print("Unfortunately, this file doesn't exist. Please make sure that you have the right spelling...")
word_filter("gini.txt") # call the function.


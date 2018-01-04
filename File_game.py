# http://stackoverflow.com/questions/8282553/removing-character-in-list-of-strings
# this program will take two  parameters one as the name of the file and another as list of words.
# by Mo
filename = "x7777.txt"
def countWords(filename, list_words):
	try:
		reading = open(filename, "r")
		check = reading.readlines()
		reading.close()
		for each in list_words: # check words in the list given
			lower = each.lower() # make sure that they are lower cause.
			count = 0
			for string in check: # loop through the file
				word_check = string.split() #  converted to a list.
				for word in word_check: #   check every word to list.
					lowerword = word.lower()
					line = lowerword.strip("!@#$%^&*()_+?><:.,-'\\ ") # clean it.
					if lower == line: # this will if what you have in the list is in file.
						count += 1 # if it is, then it will add one.
			print(lower, ":", count)
	except FileNotFoundError: # this will make that the file  exist.
			print("Unfortunately, this file doesn't exist. Please make sure that you have it spelled right...")
			for zero in list_words:# if the file does't  exist then it will print what passed in the list and 0.
				if zero != "":
					print(zero, ":", "0")
				else:
					pass
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
countWords(filename, ["success"])

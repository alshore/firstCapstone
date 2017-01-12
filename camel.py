#define main function
def main():

	# get input from user
	# set to title case and split into array
	words = raw_input("Enter text to convert: ").title().split()
	# initialize results variable
	camel = ""
	for word in words:
		# first word all lower case
		if word == words[0]:
			word = word.lower()
			# add word to results string
			camel += word
		else:
			# all other words remain in title case and 
			# get added to the results string
			camel += word
	# print results to console
	print camel
# call main function
main()
# import random module
import random
# define main function
def main():
	# generate random int between 1 and 100
	randNum = random.randint(0, 100)
	# get input from user
	guessNum = int(raw_input("Enter an integer between 1 and 100: "))
	# if numbers equal, print statement
	if randNum == guessNum:
		print "Great guess!"
	# else, enter while loop until number guessed
	else:
		while guessNum != randNum:
			if guessNum > randNum:
				print "Oops, too high."
				guessNum = int(raw_input("Guess again: "))
			elif guessNum < randNum:
				print "Oops, too low."
				guessNum = int(raw_input("Guess again: "))
			else:
				guessNum = int(raw_input("Oops, enter an integer between 1 and 100: "))
		# print statement of success
		print "Yay! You guessed correctly!"
# call main function
main()
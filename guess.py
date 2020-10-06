import random

hiddenNumber = random.randrange(0, 100)
print("Welcome to the guess game ! \n Try to guess the secret number between 0 and 100\n")
guess = int(input("Please enter your guess: "))
while guess != hiddenNumber:
	if guess == hiddenNumber:
		print("Dead on!")
	elif guess < hiddenNumber:
		print("Too low")
		guess = int(input("Please enter your guess: "))
	else:
		print("Too high")
		guess = int(input("Please enter your guess: "))
print("Amazing ! You WIN! ")

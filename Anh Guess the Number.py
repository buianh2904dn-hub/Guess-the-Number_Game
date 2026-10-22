import time

time.sleep(1)
print("Hello! Welcome to the game GUESSING NUMBER!!! ")
time.sleep(2)
print("The rule is really simple by guessing the integer from 1 to 10. (Only interger and not a float!!!)")
time.sleep(2)
print("You will have 3 times to guess the right number.")
time.sleep(2)
print("If you guess wrong all 3 times. Well... you lost :)")
time.sleep(2)
print("Now, let's get started!!! \n")

import random

time.sleep(1)
again = 'YES'



while again == 'YES' or again == 'Y':
	num = random.randint(1,10)
	guess = int(input("Guess a number from 1 to 10? "))
	
	if guess == num:
		print('Congratulations! You win at the first try!')
	else:
		print("Oh! Let's try again.")
		
		if guess < num:     #Guess for the 2 try
			guess = int(input("Let's type a higher number: "))
			if guess == num:
				print("Congratulations! You win at the second try!")
			elif guess > num:           #If it different from the num, move to the 3 try
				guess = int(input("Let's type a lower number: "))
				if guess == num:
					print("Congratulations! You win at the third try!")
				else:
					print("Uh Oh... You lost...")
			else:
				guess = int(input("Your answer is too low. Guess another number? "))
				if guess == num:
					print("Congratulations! You win at the third try!")
				else:
					print("Uh Oh... You lost...")
					
		elif guess == num:
			print("Congratulations! You win at the second try!")


		else:        #Same as line 30
			guess = int(input("Let's type a lower number: "))
			if guess == num:
				print("Congratulations! You win at the second try!")
			elif guess > num:
				guess = int(input("Your answer is too high. Guess another number? "))
				if guess == num:
					print("Congratulations! You win at the third try!")
				else:
					print("Uh Oh... You lost...")
			else:
				guess = int(input("Your answer is too low. Guess another number? "))
				if guess == num:
					print("Congratulations! You win at the third try!")
				else:
					print("Uh Oh... You lost...")
			
		
	print("The answer is " + str(num))

	again = input("Do you want to play again?(Y/N)\n").upper()
print("Thank you for playing!")
time.sleep(1)
print("Game over.")

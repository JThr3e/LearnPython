from random import randint
cont = 1
while(cont == 1):
	target = randint(0,100)
	guess = int(input("Please guess an integer from 0 to 100:   "))
	count = 1
	prev = guess
	while(guess != target):
		count = count+1
		if(abs(target-prev) > abs(target-guess)): 
			print ("Warmer!")
			prev = guess
			guess = int(input("Please guess an integer from 0 to 100:   "))
		elif(abs(target-prev) < abs(target-guess)): 
			print ("Colder!")
			prev = guess
			guess = int(input("Please guess an integer from 0 to 100:   "))
		else: 
			print ("Try Again!")
			prev = guess
			guess = int(input("Please guess an integer from 0 to 100:   "))
	print ("Congrats you guessed correctly with", count, "guesses!")
	cont = int(input("Do you want to play again? 1=yes 0=no"))


	

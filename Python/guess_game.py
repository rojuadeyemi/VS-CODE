# This is a guess the number game.
import random
def guess_number():
	print("Loading.....................100%\n\n")
	print("#"*35)
	print("#" *2+ " WELCOME TO GUESS THE NUMBER SHOW ")
	print("#"*35, "\n\n")
	print("In this game, How crazy you are is determined by your upper limit number")
	while True:
		try:
			print("what's your upper limit number?\nHINT: 5, 10, 20, 50, 100, 1000,10000,100000 etc.")
			upper = int(input(">>> "))
		except (TypeError, ValueError) as e:
			print(f"\nYou entered {e}. \nAn integer is required\n")
		else: break
		
	guesstaken = 0
	answer = []
	value = []
	correct = False
	print(f'Here we go. I am thinking of a number between 1 and {upper}.')
	
	while not correct:
		secretNumber = random.randint(1, upper)
		if guesstaken==0:
			guess =int(input("Take a guess >>> "))
		else:
			guess = int(input("Take another guess >>> "))
		guesstaken +=1
		if guess>upper or guess<1:
			print("="*35)
			print("This input is not acceptable")
			print("="*35)
			print("")
		elif guess < secretNumber:
			print("="*35)
			print('Your guess is less than the number.\n')
			print("="*35)
			print("") 
			answer.append(guess)
			value.append(secretNumber)
		elif guess > secretNumber:
			print("="*37)
			print('Your guess is higher than the number.\n')
			print("="*37)
			print("")
			answer.append(guess)
			value.append(secretNumber)
		else:
			correct = True
			print("="*46)
			print(f"Good job! You guessed my number in {guesstaken} guesses!\n")
			print("="*46)
			print("")
			print("_"*60)
			print(f" Your answers: {answer}\nGuessed numbers: {value}")
			print("_"*60)
			
			
if __name__ =="__main__":
	guess_number()
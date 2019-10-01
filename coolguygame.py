#Kaiden Haggerty
#Rock paper sissors game
#-------------------------------------------------------------------------------------------
# welcome page, with name entry
#score screen with computer, player(name), ties
# options for game r,q,p,s
# game will loop until q is entered
# each loop it will get a random choice from the computer
# a choice from the player, compare the two, and update the score
#When the game is over (q is endered) final score is displayed
#-----------------------------------------------------------------------------------------

#Imports:
import random



# Variables:
print("Welcome to Rock, Paper, Scissors")
name= input("Enter you name")
playerScore=0
computerScore=0
ties=0
# make a list:
cChoices=["r","p","s"]
#MAin loop:
while True:
	print("Score:")
	print("Computer"+ str(computerScore))
	print(name + ":" + str(playerScore))
	print("Ties"+ str(ties))
	choice= input("Enter 'r' for ROCK, 'p' for PAPER, 's' for SCISSORS, or 'q' to QUIT:")
	computerChoice= random.choice(cChoices)
	print(computerChoice)
	if choice =="q":
		break


	if choice =="r":
		print(name  +  "Picked ROCK")
		if computerChoice == "r":
			print("Computer picked ROCK")
			print("This is a tie")
			ties= ties+1

		elif computerChoice == "p":
			print("Computer picked PAPER")
			print("PAPER beats ROCK")
			computerScore+=1
		else:
			print("Computer picked SCISSORS")
			print("ROCK beats SCISSORS")
			playerScore+=1

	elif choice =="p":
		print( name  +  "Picked PAPER")
		if computerChoice=="p":
			print("Computer picked PAPER")
			print("This is a tie")
			ties= ties+1
		elif computerChoice =="s":
			print("Computer picked SCISSORS")
			print("SCISSORS beats PAPER")
			computerScore +=1
		else:
			print("Computer picked ROCK")
			print("PAPER beats ROCK")
			playerScore+=1 
	elif choice=="s":
		print( name  +  "Picked SCISSORS")
		if computerChoice=="s":
			print("Computer picked SCISSORS")
			print("This is a tie")
			ties=ties+1
		elif computerChoice=="r":
			print("Computer picked ROCK")
			print("ROCK beats SCISSORS")
			computerScore+=1
		else:
			print("Computer picked PAPER")
			print("SISSORS beat PAPER")
			playerScore+=1
	else:
		print("This is not an option")

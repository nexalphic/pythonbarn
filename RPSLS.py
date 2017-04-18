import random

choices = {
    "rock": 0,
    "paper": 1,
    "scissors": 2,
    "lizard": 3,
    "spock": 4,
}

playerScore = 0
gameOn = True

while gameOn == True:
    playerChoice = input("Rock, Paper, Scissors, Lizard, or Spock?")
   	while lower(playerChoice) not in ["rock", "paper", "scissors", "lizard", "spock", "quit"]:
        playerChoice = input("Rock, Paper, Scissors, Lizard, or Spock?")
    computerChoice = random.choice(list(choices))
    x = abs(computerChoice - playerChoice) % 5
    if lower(playerChoice) == "quit":
        break
    elif x == 0:
        print "It's a tie."
    elif x == 2 or x == 1:
        print "You win."
        playerScore += 1
    else:
        print "You lose."
        playerscore -= 1
	foundInput = False
	while foundInput == False
    	keepPlaying = lower(input("Keep playing? Y/N"))
    	if keepPlaying in ["y", "n", "yes", "no"]:
        	if keepPlaying in ["y", "yes"]:
            	foundInput == True
        	elif keepPlaying in ["n", "no"]:
                gameOn == False
                print "Your score was: " + playerScore
                foundInput == True

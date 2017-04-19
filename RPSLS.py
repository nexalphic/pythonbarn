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
    playerChoice = input("Rock, Paper, Scissors, Lizard, or Spock?").lower()
    print playerChoice
    while playerChoice not in ["rock", "paper", "scissors", "lizard", "spock", "quit"]:
        playerChoice = input("Rock, Paper, Scissors, Lizard, or Spock?")
    computerChoice = random.choice(list(choices))
    print "You chose " + playerChoice
    print "The computer chose " + computerChoice
    if playerChoice == "quit":
        break
    else:
        x = abs(choices[computerChoice] - choices[playerChoice]) % 5
        if x == 0:
            print "It's a tie."
        if x == 2 or x == 1:
            print "You win."
            playerScore += 1
        else:
            print "You lose."
            playerScore -= 1
        foundInput = False
        while foundInput == False:
            keepPlaying = input("Keep playing? Y/N").lower()
            if keepPlaying in ["y", "n", "yes", "no"]:
                if keepPlaying in ["y", "yes"]:
                    foundInput = True
                elif keepPlaying in ["n", "no"]:
                    gameOn = False
                    foundInput = True
            else:
                print "That's not yes or no."
print "Your score was: " + str(playerScore)

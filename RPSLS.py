import random
import simplegui

WIDTH = 200
HEIGHT = 200


choices = {
    "rock": 0,
    "paper": 1,
    "scissors": 2,
    "lizard": 3,
    "spock": 4,
}


playerScore = 0
gameOn = True

frame = simplegui.create_frame("Rock, Paper, Scissors, Lizard, Spock", WIDTH, HEIGHT)

foundInput = False

def input_handler():
    foundInput == True
inp = frame.add_input('Input', input_handler, 50)

playerChoice = ""
computerChoice = ""

def draw_handler(canvas):
    canvas.draw_text(str(playerScore), [100, 40], 12, "White")
    canvas.draw_text(playerChoice, [20, 100], 20, "White")
    canvas.draw_text(computerChoice, [140, 100], 20, "White")

frame.set_draw_handler(draw_handler)

    
while gameOn == True:
    playerChoice = playerChoice.lower()
    print playerChoice
    while foundInput == False:
        pass
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






frame.start()

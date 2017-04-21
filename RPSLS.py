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

frame = simplegui.create_frame("Rock, Paper, Scissors, Lizard, Spock", WIDTH, HEIGHT)

computerChoice = ""
playing = True
winOrlose = ""
playerAttack = ""
def draw_handler(canvas):
    
        canvas.draw_text(str(playerScore), [100, 40], 12, "White")
        canvas.draw_text(str(computerChoice), [140, 160], 20, "White")
        canvas.draw_text(str(playerAttack), [20, 160], 20, "White")
        if playing == False:
            canvas.draw_text(winOrlose + " Keep playing? Y/N?", [15, 100], 15, "White")
            
frame.set_draw_handler(draw_handler)

askChoice = True

def game(playerC):
    global playing
    global playerScore
    global playerAttack
    global computerChoice
    global winOrlose
    playerChoice = playerC.lower()
    if playing == True:
        if playerChoice in ["rock", "r", "paper", "p", "scissors", "s", "lizard", "l", "spock", "s"]:
            playerAttack = playerChoice
            computerChoice = random.choice(list(choices))
            print "You chose " + playerAttack
            print "The computer chose " + computerChoice
            x = abs(choices[computerChoice] - choices[playerAttack]) % 5
            if x == 0:
                winOrlose = "It's a tie."
            if x == 2 or x == 1:
                winOrlose = "You win."
                playerScore += 1
            else:
                winOrlose = "You lose."
                playerScore -= 1
            playing = False
        else:
            print "Input not accepted."
    else:
        
        if playerChoice in ["y", "n", "yes", "no"]:
            if playerChoice in ["y", "yes"]:
                pass
            elif playerChoice in ["n", "no"]:
                print "Your score was: " + str(playerScore)
            else:
                print "That's not yes or no."
            playing = True
        
    

inp = frame.add_input('Input', game, 100)





frame.start()
	

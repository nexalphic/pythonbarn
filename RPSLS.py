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

playerChoice = ""
computerChoice = ""
playing = True

def draw_handler(canvas):
    if playing == True:
        canvas.draw_text(str(playerScore), [100, 40], 12, "White")
        canvas.draw_text(playerChoice, [20, 100], 20, "White")
        canvas.draw_text(computerChoice, [140, 100], 20, "White")
    else:
        canvas.draw_text("Keep playing? Y/N?", [140, 100], 20, "White")

frame.set_draw_handler(draw_handler)

askChoice = True

def game(playerChoice):
    global askChoice
    global playerScore
    playerChoice = playerChoice.lower()
    if askChoice == True:
        playing = True
        if playerChoice in ["rock", "r", "paper", "p", "scissors", "s", "lizard", "l", "spock", "s"]:
            computerChoice = random.choice(list(choices))
            print "You chose " + playerChoice
            print "The computer chose " + computerChoice
            x = abs(choices[computerChoice] - choices[playerChoice]) % 5
            if x == 0:
                print "It's a tie."
            if x == 2 or x == 1:
                print "You win."
                playerScore += 1
            else:
                print "You lose."
                playerScore -= 1
            playing = False
        else:
            print "Input not accepted."
    else:
        
        if playerChoice in ["y", "n", "yes", "no"]:
            if keepPlaying in ["y", "yes"]:
                pass
            elif keepPlaying in ["n", "no"]:
                print "Your score was: " + str(playerScore)
            else:
                print "That's not yes or no."
            playing = True
        
    

inp = frame.add_input('Input', game, 50)





frame.start()

import simplegui
import random

wordList = ["monster", "witch", "ghost", "pirate", "pumpkin", "princess", "chocolate"]

nooseStates = {
    6: """
 _______
 |/      |
 |
 |
 |
 |
 |
_|___ 
""",
    5: """ 
 _______
 |/      |
 |      (_)
 |
 |
 |
 |
_|___ 
""",
    4: """ 
 _______
 |/      |
 |      (_)
 |       |
 |       |
 |
 |
_|___ 
""",
    3: """ 
 _______
 |/      |
 |      (_)
 |      \|
 |       |
 |
 |
_|___ 
""",
    2: """ 
 _______
 |/      |
 |      (_)
 |      \|/
 |       |
 |
 |
_|___ 
""",
    1: """ 
 _______
 |/      |
 |      (_)
 |      \|/
 |       |
 |      |
 |
_|___ 
""",
    0: """ 
 _______
 |/      |
 |      (_)
 |      \|/
 |       |
 |      | |
 |
_|___ 
""",
}
targetWord = ""
guess = ""
playing = True
cash = 100
broken = False

def confirmLetter(place, revealW, confirmW):
    revealW = list(revealW)
    revealW[place] = confirmW[place]
    return "".join(revealW)

while playing == True:
    targetWord = random.choice(wordList)
    revealedWord = "*" * len(targetWord)
    tries = 6
    win = False
    print "You have: %s ollars." % cash
    bet = int(input("Place a bet."))
    while tries > 0:
        print "The word is:" + revealedWord
        print
        print nooseStates[tries]
        guess = input("Guess what letter might be in the word or the word itself.")
        if guess == "quit":
            playing = False
            break
        elif len(guess) == 1:
            if guess in targetWord:
                for l in range(0, len(targetWord)):
                    if targetWord[l] == guess:
                        print "t"
                        revealedWord = confirmLetter(l, revealedWord, targetWord)
                        
            else:
                tries -= 1
        elif len(guess) > 1:
            if guess == targetWord:
                revealedWord = targetWord
                win = True
                print "The word is: " + targetWord
                break
            else:
                tries -= 1
        else:
            print "You didn't even put in anything..."
    if win == True:
        print "You win!"
        cash += bet
    else:
        print "You lost..." 
        cash -= bet

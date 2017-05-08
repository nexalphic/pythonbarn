import simplegui
import random

WIDTH = 600
HEIGHT = 600

states = {
    0: "empty",
    1: "x",
    2: "o"
}

colors = ("Black", "Red", "Orange", "Yellow", "Green", "Blue", "Purple")
color = 0
          
def wipeGrid():
    global grid
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
        ]
    
wipeGrid()
playing = "start"
c_text = [0, "", 0, "White", "White"]
player_piece = True
computer_piece = True
turn = random.choice(range(1, 3))
tie = False
#1 = X, 2 = O


def mouseZone(position):
    zone = []
    for axis in range(1, -1, -1):
        if position[axis] < 200:
            zone.append(0)
        elif position[axis] < 400:
            zone.append(1)
        else:
            zone.append(2)
    return zone


def centerText(text):
    global c_text
    if text == "start":
        c_text = [249, "or", 120, "White", "White"]
    elif text == "X_wins":
        c_text = [225, "win", 96, "Green", "White"]
    elif text == "O_wins":
        c_text = [225, "win", 96, "White", "Green"]
    elif text == "tie":
        c_text == [225, "tie", 96, "White", "White"]
    else:
        c_text[1] = ""


        
centerText(playing)       

grid[1][2] = 1
grid[1][0] = 2


def ai(grid):
    global tie
    found_move = False
    times = 0
    while found_move == False and times < 27:
        #random grid location
        random_x = random.randrange(0, 3)
        random_y = random.randrange(0, 3)
        if grid[random_y][random_x] != 1 and grid[random_y][random_x] != 2:
            grid[random_y][random_x] = computer_piece
            found_move = True
        else:
            times += 1
    if times >= 27:
        tie = True

def winDetect(grid):
    for i in range(0, 3):
        if grid[i][0] == grid[i][1] == grid[i][2] != 0:
            return grid[i][0]
            break
        elif grid[0][i] == grid[1][i] == grid[2][i] != 0:
            return grid[0][i]
            break
    if grid[0][0] == grid[1][1] == grid[2][2] != 0:
        return grid[0][0]
    if grid[0][2] == grid[2][2] == grid[2][0] != 0:
        return grid[0][2]
            
def setup():
    global playing
    global player_piece
    global computer_piece
    wipeGrid()
    centerText("game")
    playing = "game"
    if random.choice([True, False]) == True:
        ai(grid)
    if player_piece == 1:
        computer_piece = 2
    else:
        computer_piece = 1
    
def mouse_handler(position):
    global grid
    global playing
    global player_piece
    global computer_choice
    zone = mouseZone(position)
    if playing == "start":
        centerText("start")
        if zone == [1, 0]:
            #Option O
            player_piece = 2
            setup()
        elif zone == [1, 2]:
            #Option X
            player_piece = 1
            setup()
    elif playing == "game":
        if grid[zone[0]][zone[1]] != 1 and grid[zone[1]][zone[0]] != 2:
            grid[zone[0]][zone[1]] = player_piece
            ai(grid)
        if tie == True:
            print "It's a tie!"
            centerText("tie")
        elif winDetect(grid) == 1 or winDetect(grid) == 2:
            if winDetect(grid) == 1:
                centerText("X_wins")
                print "X wins!"
            elif winDetect(grid) == 2:
                centerText("O_wins")
                print "O wins!"


frame = simplegui.create_frame("Tic Tac Toe", WIDTH, HEIGHT)

frame.set_mouseclick_handler(mouse_handler)

frame.set_canvas_background('Black')
          
def key_handler(key):
    global color
    global colors
    if key == simplegui.KEY_MAP['r']:
            color += 1       
            frame.set_canvas_background(colors[color % 7])
            
frame.set_keydown_handler(key_handler)

def draw_handler(canvas):
    global grid
    global c_text
    canvas.draw_line((200, 20), (200, 580), 5, "White")
    canvas.draw_line((400, 20), (400, 580), 5, "White")
    canvas.draw_line((20, 200), (580, 200), 5, "White")
    canvas.draw_line((20, 400), (580, 400), 5, "White")
    canvas.draw_text(c_text[1], (c_text[0], 330), c_text[2], "White")
    for y in xrange(len(grid)):
        for x in xrange(len(grid[y])):
            state = grid[y][x]
            if state == 1:
                canvas.draw_line((x*200+20, y*200+20), (x*200+180, y*200+180), 7, c_text[3])
                canvas.draw_line((x*200+180, y*200+20), (x*200+20, y*200+180), 7, c_text[3])
            elif state == 2:
                canvas.draw_circle((x*200+100, y*200+100), 80, 7, c_text[4])
                            
frame.set_draw_handler(draw_handler)

frame.start()

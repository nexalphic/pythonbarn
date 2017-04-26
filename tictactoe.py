import simplegui
import random

WIDTH = 600
HEIGHT = 600

states = {
    0: "empty",
    1: "x",
    2: "o"
}

def wipe_grid():
    global grid
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
        ]
    
wipe_grid()
playing = "start"
print_grid = False
c_text = []
player_piece = True
#1 = X, 2 = O

def mouse_zone(position):
    zone = []
    for axis in (0, 1):
        if position[axis] < 200:
            zone.append(1)
        elif position[axis] < 400:
            zone.append(2)
        else:
            zone.append(3)
    return zone

def center_text(text):
    if text == "start":
        c_text = [210, "or", 15]
    elif text == "wins":
        c_text = [205, "wins", 11]
    else:
        c_text[1] = ""

def mouse_handler(position):
    global grid
    zone = mouse_zone(position)
    if playing == "start":
        c_text("start")
        grid[1][0] = 1
        grid[1][2] = 2
        if zone == [1, 0]:
            player_piece = 1
        elif zone == [1, 2]:
            player_piece = 2
            playing = "game"
    if playing == "game":
        grid[zone[0]][zone[1]] = player_piece
        
        
def mark_draw(zone):
    global grid
    if grid[x][y] == "x":
        canvas.draw_line((x*200+20, y*200+20), (x*200+180, y*200+180), 7, "White")
    else:
        canvas.draw_line((x*200+100, y*200+100), 80, 7, "White")
            
frame = simplegui.create_frame("Tic Tac Toe", WIDTH, HEIGHT)

frame.set_mouseclick_handler(mouse_handler)

def draw_handler(canvas):
    global grid
    if print_grid == True:
        canvas.draw_line((200, 20), (200, 580), 5, "White")
        canvas.draw_line((400, 20), (400, 580), 5, "White")
        canvas.draw_line((20, 200), (580, 200), 5, "White")
        canvas.draw_line((20, 400), (580, 400), 5, "White")
    for x in xrange(len(grid)):
        for y in xrange(len(grid(x))):
                mark_draw(grid[x][y], x, y)
                            
frame.set_draw_handler(draw_handler)



frame.start()

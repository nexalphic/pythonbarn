import simplegui

WIDTH = 600
HEIGHT = 600

states = {
    0: "empty",
    1: "x",
    2: "o"
}

}

def mouse_handler(position):
    zone = []
    for axis in (0, 1):
        if position[axis] < 200:
            zone.append(1)
        elif position[axis] < 400:
            zone.append(2)
        else:
            zone.append(3)
    return zone
        
def game():
    playing = True
    while playing == True:
        

frame = simplegui.create_frame("Tic Tac Toe", WIDTH, HEIGHT)

frame.set_mouseclick_handler(mouse_handler)

def draw_handler(canvas):
    canvas.draw_line((200, 20), (200, 580), 5, "White")
    canvas.draw_line((400, 20), (400, 580), 5, "White")
    canvas.draw_line((20, 200), (580, 200), 5, "White")
    canvas.draw_line((20, 400), (580, 400), 5, "White")

frame.set_draw_handler(draw_handler)



frame.start()

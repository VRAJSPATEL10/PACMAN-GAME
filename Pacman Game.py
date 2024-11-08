from random import choice
from turtle import *

from freegames import floor, vector
f=open("score.txt","a+") #  writes score in file to fetch max-score
state = {'score': 0} #dictionary that maintains score
m=0 
path = Turtle(visible=False)    #object to create path
writer = Turtle(visible=False)  #object to write score
text=Turtle(visible=False)      #object to write heading pacman game
maxscr=Turtle(visible=False)    #object to write max-score
newhighscr=Turtle(visible=False)    
gameover=Turtle(visible=False)
aim = vector(10, 0) #to initilaize movement of pacman
pacman = vector(-40, -80)   #to initilaize positon of pacman
ghosts = [
    [vector(-180, 160), vector(10, 0)],
    [vector(-180, -160), vector(0,10)],
    [vector(100, 160), vector(0, -10)],
    [vector(100, -160), vector(-10, 0)],
] #to initlaize positon of ghost
# to make logic of creating map
#1->blue background white dot
#2->black background
tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
    0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
] 
# fmt: on


def square(x, y):
    """Draw square using path at (x, y)."""
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()
# make a 20*20 square 
    for count in range(4):
        path.forward(20)
        path.left(90)

    path.end_fill()


def offset(point):
    """Return offset of point in tiles."""
    x = (floor(point.x, 20) + 200) / 20 #converts pixels into turtle graphics unit
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index


def valid(point):
    """Return True if point is valid in tiles."""
    index = offset(point)

    if tiles[index] == 0:
        return False

    index = offset(point + 19)

    if tiles[index] == 0:
        return False

    return point.x % 20 == 0 or point.y % 20 == 0


def world():
    """Draw world using path."""
    bgcolor('black')
    path.color('blue')

    for index in range(len(tiles)):
        tile = tiles[index]

        if tile > 0:
            x = (index % 20) * 20 - 200 #to convert turtle graphic units (1,0) into pixels
            y = 180 - (index // 20) * 20
            square(x,y)

            if tile == 1:
                path.up()
                path.goto(x + 10, y + 10) #to print dot in blue bacground tiles
                path.dot(5, 'white')


def move():
    """Move pacman and all ghosts."""
    global m
    writer.undo()
    writer.write("SCORE:"+str(state['score']),align='center',font=("Arial", 24, "normal"))
    if(state['score']>m):
        newhighscr.goto(-10,-320)
        newhighscr.color('red')
        newhighscr.write("NEW HIGHSCORE",align='center',font=("Arial", 24, "normal"))
        maxscr.undo()
        maxscr.write("HIGHSCORE:"+str(state['score']),align='center',font=("Arial", 24, "normal"))
    clear()
    if valid(pacman + aim): #will move the pacman if given index in aim is correct
        pacman.move(aim)

    index = offset(pacman) 

    if tiles[index] == 1:
        tiles[index] = 2 #if pacman willmove through white dot it will eat dot 
        state['score'] += 1 #increases the score 
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20 
        square(x, y)

    up()
    goto(pacman.x + 10, pacman.y + 10) 
    dot(20, 'yellow')

    for point, course in ghosts:
        if valid(point + course):
            point.move(course)
        else:
            options = [
                vector(10, 0),
                vector(-10, 0),
                vector(0, 10),
                vector(0, -10),
            ]
            plan = choice(options)
            course.x = plan.x
            course.y = plan.y

        up()
        goto(point.x + 10, point.y + 10)
        dot(20, 'red')

    update()

    for point, course in ghosts:
        if abs(pacman - point) < 20:
            gameover.goto(-25,200)
            gameover.color('red')
            gameover.write("GAME OVER",align='center',font=("Arial", 24, "normal"))
            return

    ontimer(move, 100)
    

def change(x, y):
    """Change pacman aim if valid."""
    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y

setup(width=1.0, height=1.0) 
hideturtle() #hide cursor
tracer(False) #dont show making of rectangles
writer.goto(-20,-220)   
writer.color('yellow')
writer.write("SCORE:"+str(state['score']),align='center',font=("Arial", 24, "normal"))
text.goto(-10,250)
text.color('yellow')
text.write('PAC-MAN GAME',align='center',font=("Arial", 50, "normal"))
f1=open("score.txt","r")
a=f1.read().split()
for i in a:
    if(int(i)>m):
        m=int(i)
maxscr.goto(-10,-270)
maxscr.color('yellow')
maxscr.write("HIGHSCORE:"+str(m),align='center',font=("Arial", 24, "normal"))
listen() #to take user input keys
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
world() #draws layout of game 
move() #moves pacmain and ghost
done() 
f1.close()
f.write(str(state['score'])+"\n")
f.close()


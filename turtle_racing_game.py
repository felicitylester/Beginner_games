# 🐢TURTLE RACING

import turtle       # allow 2D graphics
import time
import random

# constants for turtle graphics
WIDTH, HEIGHT = 500, 500
COLORS = ['darkred', 'royalblue', 'magenta', 'forestgreen', 'blue', 'violet', 'brown', 'grey', 'pink', 'darkorange' ]


print('     WELCOME TO 🐢TURTLE RACING\n')

# Get information from user and check it is valid
def get_number_of_racers():
    racers = 0
    while True:
        racers = input('How many turtles do you want to race (2-10)? ')
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Invalid. Number is not numeric. Try again... : ")
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print('Number not in range 2-10. Try again... : ')


# Create and customize a turtle object google example
# my_turtle = turtle.Turtle()
# my_turtle.shape("turtle")  # Options: 'arrow', 'classic', 'turtle', 'circle'
# my_turtle.color("blue")    # Set pen/turtle color
# my_turtle.speed(3)         # Speed from 1 (slow) to 10 (fast). 0 is fastest.


# Create the turtles - assign each turtle a different color & position them at the starting line
def create_turtles(colors):
    turtles = []
    spacing_x = WIDTH // (len(colors) + 1)      # dynamically space the turtles depending on # of racers

    # match random colors to number of racers
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)      # point upwards
        racer.penup()       # keep pen from making while positioning
        racer.setpos(-WIDTH // 2 + (i + 1) * spacing_x, -HEIGHT // 2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles


# Start the race - randomly move each turtle forward until one reaches the finish line
def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)      # min value gives slower speed
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]     # returns the winner


# create the graphics window
def init_turtle():
    screen = turtle.Screen()
    # screen.bgcolor()
    screen.setup(WIDTH, HEIGHT)
    screen.title('🐢 TURTLE RACING! 🐢')

racers = get_number_of_racers()
init_turtle()
random.shuffle(COLORS)
colors = COLORS[:racers]

# Display the winner
winner = race(colors).upper()
print('The winning turtle is 🐢', winner, ' 🏁')

time.sleep(10)      # time till window closes

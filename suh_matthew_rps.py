# This file was created by: Matthew Suh

'''
Primary goal: When a user clicks on their choice, the computer will randomly choose and option and display the results. For this project, I worked closely with Jack Gately and Roan Kher (my table mates) when debugging code or when issues arised.
'''

# Import necessary libraries for graphics, photos, etc. 
import turtle
from turtle import *
import os

# Print the current working directory using different methods. Roan helped me with this portion. 
print("The current working directory is (getcwd): " + os.getcwd())
print("The current working directory is (path.dirname): " + os.path.dirname(__file__))

# Set up folders for the game and images.
game_folder = os.path.dirname(__file__)
images_folder = os.path.join(game_folder, 'images')

# Defining the exact width and height of the game window.
WIDTH, HEIGHT = 1000, 400

# Setting the dimensions for the rock, paper, and scissor images.
rock_w, rock_h = 256, 280
paper_w, paper_h = 256, 204
scissors_w, scissors_h = 256, 170

# Initializes the game screen with a specific size and appearance. 
screen = turtle.Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)  
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg="lightblue")

# Creates the game window to not be resizable.
cv = screen.getcanvas()
cv._rootwindow.resizable(False, False)

# Sets up the rock image and creates a turtle object to display it. 
rock_image = os.path.join(images_folder, 'rock.gif')
rock_instance = turtle.Turtle()

# Sets up the paper image and creates a turtle object to display it. 
paper_image = os.path.join(images_folder, 'paper.gif')
paper_instance = turtle.Turtle()

# Sets up the scissors image and creates a turtle object to display it. 
scissors_image = os.path.join(images_folder, 'scissors.gif')
scissors_instance = turtle.Turtle()

"""
The three functions below display the rock, paper, and scissors images at specified coordinates. 
The images represent what the user chooses in the game. 
The images are loaded into the turtle graphics library and subsequently positioned on the screen
"""

def show_rock(x,y):
    screen.addshape(rock_image)
    rock_instance.shape(rock_image)
    rock_instance.penup()
    rock_instance.setpos(x,y)

def show_paper(x,y):
    screen.addshape(paper_image)  
    paper_instance.shape(paper_image) 
    paper_instance.penup()  
    paper_instance.setpos(x,y)

def show_scissors(x,y):
    screen.addshape(scissors_image)
    scissors_instance.shape(scissors_image)
    scissors_instance.penup()
    scissors_instance.setpos(x,y)

# Creates turtles for the text display.
t = turtle.Turtle()
text = turtle.Turtle()
text.color('deep pink')

# Hides the turtle graphics cursor (line) for both turtles.
t.penup()
text.hideturtle()
t.hideturtle()

# Shows the rock, paper, and scissors at their initial positions.
show_rock(-300, 0)
show_paper(0,0)
show_scissors (300,0)

# Sets up the text to prompt/ask the user for their choice.
text.penup()
text.hideturtle()
text.setpos(-300,150)
text.write("What do you choose, rock, paper, or scissors?", False, "left", ("Arial", 24, "normal"))

# The following function checks to see if the user's click position (x,y) collides with an object's position and dimensions (width and height). 
def collide(x,y,obj,w,h):
    if x < obj.pos()[0] + w/2 and x > obj.pos()[0] - w/2 and y < obj.pos()[1] + h/2 and y > obj.pos()[1] - h/2:
        return True
    else:
        return False
    t.penup()

# The following function handles the user's choice and determines/calculates the game result. 
def player(x, y): 
    global text

    if (collide(x,y,rock_instance, rock_w, rock_h)):
        user_choice = "rock"
    elif(collide(x,y,paper_instance,rock_w,rock_h)):
        user_choice = "paper"
    elif(collide(x,y,scissors_instance,scissors_w,scissors_h)):
        user_choice = "scissors"

# Clears all the text on the screen.
    text.penup()
    text.clear()  

# Sets up the position for displaying the user's choice.
    text.goto(-120, 150)
    text.write(f"You chose {user_choice}!", align="left", font=("Arial", 24, "normal"))

# Import the randint function from the random module.
    from random import randint

# Creates a list of choices for the computer to choose from.
    choices = ["rock", "paper", "scissors"]

# Randomly selects a choice for the computer to display.
    computer = choices[randint(0, 2)]

# Creates a message to display the computer's choice.
    message = f"Computer chooses... {computer}!"
    x, y = -190, -200
    target_x, target_y = -200, -200

# Sets up the text that will display the computer's choice.
    text.penup()
    text.goto(x, y)
    text.write(message, align="left", font=("Arial", 24, "normal"))
    text.goto(target_x, target_y)

# Import the time module to create a brief pause in the game. Roan Kher helped explain what this does and how to make it work.
    import time

# Pauses the game program for 1 second.
    time.sleep(1)

# Determines the game result based on the user's and computer's choices.
    if user_choice == computer:
        result = "It's a tie! Try again!"
    elif (user_choice == "rock" and computer == "scissors") or \
         (user_choice == "paper" and computer == "rock") or \
         (user_choice == "scissors" and computer == "paper"):
        result = "Congratulations! You WON!"
    else:
        result = "Sorry, you LOST!"

# Clears the text and sets up the display for the game result.
    text.clear()
    text.goto(-140, 150)
    text.write(result, align="left", font=("Arial", 24, "normal"))
    
# Detects the user's click and calls the player function when a click occurs. 
playerchoice = screen.onclick(player)

# Runs the game loop, so the user can keep playing the game if they please. 
playerchoice = screen.mainloop()
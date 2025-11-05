
# feel free to change the window size
WIDTH = 600
HEIGHT = 600

# create any necessary variables here


def setup():
    # load any necessary images here
    pass


def move():
    # move objects here
    pass


def checkCollisions():
    # check for collisions between objects here
    pass


def draw(canvas):
    # draw your game here
    pass


def keyPressed(key):
    # handles what should happen when a key is pressed
    pass


def keyReleased(key):
    # handles what should happen when a key is released
    pass




# ************** DON'T TOUCH THE BELOW CODE ***************************
import pygame, sys
from pygame.locals import *
import random
# always need this - starts the graphics
pygame.init()
pygame.font.init()
fps = pygame.time.Clock()
pygame.font.init()
myfont = pygame.font.SysFont('Times New Roman', 30)
window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Pong')
setup()
# loop to keep the game continuously running
while True:

    # update any variables
    move()
    checkCollisions()

    # draw our graphics
    draw(window)

    # this cycles through all the events that may happen during the game
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            keyPressed(event.key)
        elif event.type == KEYUP:
            keyReleased(event.key)
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()

    # update the graphics display
    pygame.display.update()

    # 30 fps
    fps.tick(30)
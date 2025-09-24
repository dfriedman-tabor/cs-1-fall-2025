# filler code for graphics with key controls

# feel free to change the window size
WIDTH = 600
HEIGHT = 600


# your variables here



def draw(canvas):
    canvas.fill((255,255,255))



def move():
    pass


# handles what should happen when a key is pressed
# note that this only activates once per press - it does not
# activate repeatedly if the key is held down
def keyPressed(key):
    if key == pygame.K_SPACE:
        pass

    if key == pygame.K_g:
        pass


# handles what should happen when a key is released
def keyReleased(key):
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

# loop to keep the game continuously running
while True:

    # update any variables
    move()

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
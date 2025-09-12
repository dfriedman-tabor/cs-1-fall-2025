# template code for you to fill in when creating basic pygame art


# dimensions of the window
width = 600
height = 800

def draw(canvas):

    pygame.draw.rect(canvas, (255, 0, 0), (0, 50, 600, 50))
    pygame.draw.rect(canvas, (255, 0, 0), (300, 300, 50, 50))

    pygame.draw.circle(canvas, (0, 255, 0), (300, 300), 40)







# don't touch the below code!
################################

import pygame, sys
from pygame.constants import KEYDOWN
from pygame.locals import QUIT

pygame.init()
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Graphics Starter')
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
while True:
    draw(window)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()




















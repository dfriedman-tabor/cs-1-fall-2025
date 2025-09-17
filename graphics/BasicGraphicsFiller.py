# template code for you to fill in when creating basic pygame art


# dimensions of the window
width = 800
height = 600

def draw(canvas):
    canvas.fill((255, 255, 255))

    # draws a circle at location (300, 100), with radius 100
    pygame.draw.circle(canvas, (255,0,0), (300, 100), 100)

    # draws a rectangle at location (200, 40), with width of 50 and height of 75
    pygame.draw.rect(canvas, (0,0,255), (200, 40, 50, 75))

    # draws a line that connects points (100, 100) and (300, 300)
    pygame.draw.line(canvas, (255, 0, 255), (100, 100), (300, 300), 3)

    # draws a triangle connecting the three points listed
    pygame.draw.polygon(canvas, (0, 0, 255), [(200, 200), (500, 300), (300, 500)])



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



import pygame
from pygame.draw import *

pygame.init()

FPS = 30
display_x = 400
display_y = 400
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE =  (0,   0, 255)
GREEN = (0, 255, 0)
RED =   (255, 0, 0)
yellow = (255, 255, 0)

screen = pygame.display.set_mode((display_x, display_y))
screen.fill(WHITE)

def smile():
    circle(screen, yellow, (display_x/2, display_y/2), display_x/2*0.8)
    circle(screen, BLACK, (display_x / 2, display_y / 2), display_x / 2 * 0.8, 2)

    rect(screen, BLACK, (display_x/2-0.2*display_x, display_y/3*2, display_x*0.4, display_y*0.1))

    circle(screen, RED, (display_x / 2 - 0.18*display_x, display_y / 2.5), display_x*0.1)
    circle(screen, BLACK, (display_x / 2 - 0.18 * display_x, display_y / 2.5), display_x * 0.1, 2)
    circle(screen, BLACK, (display_x / 2 - 0.18 * display_x, display_y / 2.5), display_x * 0.05)
    circle(screen, RED, (display_x / 2 + 0.18*display_x, display_y / 2.5), display_x*0.08)
    circle(screen, BLACK, (display_x / 2 + 0.18*display_x, display_y / 2.5), display_x*0.08, 2)
    circle(screen, BLACK, (display_x / 2 + 0.18 * display_x, display_y / 2.5), display_x * 0.04)

    line(screen, BLACK, [display_x / 2 - 0.1*display_x, display_y / 3.5], [display_x / 2 - 0.4*display_x, display_y / 5], 20)
    line(screen, BLACK, [display_x / 2 + 0.1 * display_x, display_y / 3.5],
         [display_x / 2 + 0.4 * display_x, display_y / 5], 20)


color = (255, 255, 255)


smile()
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
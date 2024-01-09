import pygame
from pygame.locals import *

pygame.init()

screen_w, screen_h = 500, 500
screen = pygame.display.set_mode((screen_w, screen_h))

while True:

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

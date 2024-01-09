import pygame
from pygame.locals import *

pygame.init()

screen_w, screen_h = 500, 500
screen = pygame.display.set_mode((screen_w, screen_h))


red = (255,0,0)
blue = (0,0,255)

drawing = False
points = []

while True:

    screen.fill((100,100,100))

    if len(points) > 1:
        r = pygame.draw.lines(screen,red,True,points,1)
        pygame.draw.rect(screen,blue,r,1)
    pygame.display.update()
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == MOUSEBUTTONDOWN:
            points.append(event.pos)
            drawing = True
        elif event.type == MOUSEBUTTONUP:
            drawing = False
        elif event.type == MOUSEMOTION and drawing:
            points[-1] = event.pos
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                if len(points) > 0:
                    points.pop()

import pygame
from pygame.locals import *
import random

def random_points(num_points):
    points = [(random.randint(0, 500), random.randint(0, 500)) for _ in range(num_points)]
    return points

pygame.init()

screen_w, screen_h = 500, 500
screen = pygame.display.set_mode((screen_w, screen_h))

points = random_points(100)
rect = Rect((50,100,200, 150))

while True:

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == KEYDOWN:
            if event.key == K_r:
                points = random_points(100)
    
    screen.fill((100,100,100))
    pygame.draw.rect(screen,(0,255,0),rect , 1)

    for p in points:
        if rect.collidepoint(p):
            pygame.draw.circle(screen,(255,0,0), p,4,0)
        else:
            pygame.draw.circle(screen,(0,0,255), p,4,0)
    
    pygame.display.flip()

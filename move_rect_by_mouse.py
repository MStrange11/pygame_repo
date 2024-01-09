# from rect import *
from pygame.locals import *
import pygame

pygame.init()

screen_w, screen_h = 500, 500
screen = pygame.display.set_mode((screen_w, screen_h))

rect0 = Rect(50, 60, 200, 80)
rect = rect0.copy()

moving = False

while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        elif event.type == MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                moving = True
        elif event.type == MOUSEBUTTONUP:
            moving = False
        elif event.type == MOUSEMOTION and moving:
            rect.move_ip(event.rel)

    
    screen.fill((100,100,100))

    pygame.draw.rect(screen,(255,255,0), rect.union(rect0))
    pygame.draw.rect(screen,(0,255,0), rect.clip(rect0))
    pygame.draw.rect(screen, (0,0,255), rect0, 1)
    pygame.draw.rect(screen, (255,0,0), rect, 4)
    pygame.display.flip()



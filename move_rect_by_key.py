# from rect import *
from pygame.locals import *
import pygame

pygame.init()

screen_w, screen_h = 500, 500
screen = pygame.display.set_mode((screen_w, screen_h))

rect0 = Rect(50, 60, 200, 80)
rect = rect0.copy()

dir = {K_LEFT: (-5, 0), K_RIGHT: (5, 0), K_UP: (0, -5), K_DOWN: (0, 5),}
dir2 = {K_4: (-5, 0), K_6: (5, 0), K_8: (0, -5), K_2: (0, 5)}


while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key in dir:
                v = dir[event.key]
                rect.move_ip(v)
            if event.key in dir2:
                v = dir2[event.key]
                rect.inflate_ip(v)
    screen.fill((100,100,100))

    pygame.draw.rect(screen,(255,255,0), rect.union(rect0))
    pygame.draw.rect(screen,(0,255,0), rect.clip(rect0))
    pygame.draw.rect(screen, (0,0,255), rect0, 1)
    pygame.draw.rect(screen, (255,0,0), rect, 4)
    pygame.display.flip()



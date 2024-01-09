import pygame
from pygame.locals import *

pygame.init()

screen_w, screen_h = 500, 500
screen = pygame.display.set_mode((screen_w, screen_h))

rect = Rect(40,10,30,20)
v= [1,1]

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    rect.move_ip(v)

    if rect.left < 0:
        v[0] *= -1
    elif rect.right > screen_w:
        v[0] *= -1
    elif rect.top < 0:
        v[1] *= -1
    elif rect.bottom > screen_h:
        v[1] *= -1

    screen.fill((100,100,100))
    pygame.draw.rect(screen, (255,0,0), rect)
    pygame.display.update()

    
        

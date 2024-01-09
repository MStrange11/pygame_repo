import pygame
from pygame.locals import *

pygame.init()

screen_w, screen_h = 500, 500
screen = pygame.display.set_mode((screen_w, screen_h))


red = (255,0,0)

start,size =(0,0),(0,0)
drawing = False
rect_list = []

while True:

    screen.fill((100,100,100))
    for r in rect_list:
        pygame.draw.rect(screen,red,r,2,5)
    pygame.draw.rect(screen,(0,255,0),(start, size),1,3)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == MOUSEBUTTONDOWN:
            start = event.pos
            size = 0,0
            drawing = True
        elif event.type == MOUSEBUTTONUP:
            end = event.pos
            size = end[0] - start[0], end[1] - start[1]
            rect = pygame.Rect(start,size)
            rect_list.append(rect)
            drawing = False
        elif event.type == MOUSEMOTION and drawing:
            end = event.pos
            size = end[0] - start[0], end[1] - start[1]

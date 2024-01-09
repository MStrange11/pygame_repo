import pygame
from pygame.locals import *
from math import *

pygame.init()

screen_w, screen_h = 1000, 700
screen_c = (screen_w // 2, screen_h // 2)
screen = pygame.display.set_mode((screen_w, screen_h))

draw = False
xy = [0, 0]

font = pygame.font.Font("freesansbold.ttf", 32)

def distance(xy):
    xd = pow(abs(screen_c[0] - xy[0]),2)
    yd = pow(abs(screen_c[1] - xy[1]),2)
    dis = sqrt(xd + yd)

    return dis

def dis_cm(dis_pixel):
    dis_in_cm = (dis_pixel / 96) * 2.54
    return dis_in_cm

move_xy = list(screen_c)

returning_speed = 1


while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == MOUSEMOTION:
            xy = pygame.mouse.get_pos()
            

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                draw = True

        if event.type == MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button
                draw = False
    
    pygame.draw.line(screen, (0, 255, 0), (0,screen_h//2), (screen_w,screen_h//2), 3)
    pygame.draw.line(screen, (255, 0, 0), (screen_w//2,0), (screen_w//2,screen_h), 3)

    if draw and screen.get_rect().collidepoint(xy):
        line = pygame.draw.line(screen, (255, 255, 255), screen_c, xy, 3)

    dis = distance(move_xy)

    text = font.render(f"{round(dis,2)} pixel",True,(255,255,255),(0,100,0))
    textRect = text.get_rect()
    textRect.topleft =  (0,0)

    dis_in_cm = dis_cm(dis)

    text2 = font.render(f"{round(dis_in_cm,2)} cm",True,(255,255,255),(0,100,100))
    textRect2 = text2.get_rect()
    textRect2.topleft =  (0,40)

    pygame.draw.circle(screen, (255,255,255), screen_c,2)
    
    if pygame.mouse.get_focused():
        pygame.draw.circle(screen, (255,255,255), xy,60, 2)
        move_xy = list(xy)
    else:
        if move_xy[0] > screen_c[0]:
            move_xy[0] -= returning_speed
        elif move_xy[0] < screen_c[0]:
            move_xy[0] += returning_speed

        if move_xy[1] > screen_c[1]:
            move_xy[1] -= returning_speed
        elif move_xy[1] < screen_c[1]:
            move_xy[1] += returning_speed
        pygame.draw.circle(screen, (255,255,255), move_xy,60, 2)
    
    pygame.draw.line(screen, (255, 0, 0), (screen_w//2,0), (screen_w//2,screen_h), 3)


    screen.blit(text, textRect)
    screen.blit(text2, textRect2)

    pygame.display.flip()
    pygame.display.update()

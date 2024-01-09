import pygame
from pygame.locals import *

pygame.init()

width, height = 600, 600

screen = pygame.display.set_mode((width,height))

black = (0,0,0)
red = (255, 0, 0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
cyan = (0,255,255)
magenta = (200,0,255)
white = (255,255,255)

key_dict = {K_k:black, K_r:red, K_g:green, K_b:blue,K_y:yellow, K_c:cyan, K_m:magenta, K_w:white}

bg = white

while True:

    screen.fill(bg)
    pygame.display.update()

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
        
        if event.type == KEYDOWN:
            if event.key in key_dict:
                bg = key_dict[event.key]
                caption = "bg-color" + str(bg)
                pygame.display.set_caption(caption)
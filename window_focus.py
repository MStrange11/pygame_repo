import pygame
from pygame.locals import *
from math import *

pygame.init()

clock = pygame.time.Clock()

screen_w, screen_h = 1200, 730
screen_c = (screen_w // 2, screen_h // 2)
screen = pygame.display.set_mode((screen_w, screen_h))

pygame.display.set_caption(f"{screen_w} , {screen_h}")

draw = False
xy = [0, 0]

font_size = 20
font = pygame.font.Font("freesansbold.ttf", font_size)

def distance(xy):
    xd = pow(abs(screen_c[0] - xy[0]),2)
    yd = pow(abs(screen_c[1] - xy[1]),2)
    dis = sqrt(xd + yd)

    return dis

def dis_cm(dis_pixel, ppi = 124):
    dis_in_cm = (dis_pixel / ppi) * 2.54
    return dis_in_cm

def show_text(txt,y, txt_bg = (100,100,100)): # display text
    text = font.render(txt,True,(255,255,255),txt_bg)
    textRect = text.get_rect()
    textRect.topleft =  (0,y)

    screen.blit(text,textRect)

move_xy = list(screen_c)

returning_speed = 1 
returning_speedX = returning_speed 
returning_speedY = returning_speed

snap = False
pause = True
ppi = 124
snap_dis = 20


while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == MOUSEMOTION:
            xy = pygame.mouse.get_pos()
            

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1 and pygame.mouse.get_focused():  # Left mouse button
                pygame.draw.line(screen, (255, 255, 255), screen_c, xy, 3)

        elif event.type == MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button
                draw = False
        
        if event.type == KEYDOWN:
            if event.key == K_p:
                ppi += 1
            if event.key == K_o:
                ppi -= 1
            if event.key == K_s:
                snap = not snap
            if event.key == K_k:
                pause = not pause

    
    pygame.draw.line(screen, (0, 255, 0), (0,screen_h//2), (screen_w,screen_h//2), 3) # x axis
    pygame.draw.line(screen, (255, 0, 0), (screen_w//2,0), (screen_w//2,screen_h), 3) # y axis

    yellow_line_len = abs(screen_w//2 - xy[0])
    blue_line_len = abs(screen_h//2 - xy[1])

    dis = distance(move_xy)

    dis_in_cm = dis_cm(dis, ppi)

    show_text(f"{round(dis,2)} pixel",0, (0,200,200))
    show_text(f"{round(dis_in_cm,2)} cm",25, (0,200,100))
    show_text(f"{ppi} ppi",50, (0,100,200))
    show_text(f"Snap : " +("on" if snap else "off"),75, (150,100,20))
    show_text(f"yellow line {yellow_line_len}",100, (150,100,20))
    show_text(f"blue line {blue_line_len}",125, (150,100,20))
    show_text(f"line diff {abs(yellow_line_len - blue_line_len)}",150, (150,100,20))

    pygame.draw.circle(screen, (255,255,255), screen_c,4) # center dot
    
    if pygame.mouse.get_focused() and pause:
        move_xy = list(xy)
        if snap and abs(yellow_line_len - blue_line_len) <= snap_dis:
            min_len = min(yellow_line_len,blue_line_len)
            draw = True

            if xy[0] < screen_w //2 and xy[1] < screen_h //2:
                # second qdar
                show_text(f"section 2",175, (150,100,20))
                move_xy = [(screen_w//2) - min_len,(screen_h//2) -  min_len] #done

            elif xy[0] > screen_w //2 and xy[1] < screen_h //2:
                # first qdar
                show_text(f"section 1",175, (150,100,20))
                move_xy = [(screen_w//2) + min_len,(screen_h//2) -  min_len] # done

            elif xy[0] < screen_w //2 and xy[1] > screen_h //2:
                # third qdar
                show_text(f"section 3",175, (150,100,20))
                move_xy = [(screen_w//2) - min_len,(screen_h//2) +  min_len]  # done

            elif xy[0] > screen_w //2 and xy[1] > screen_h //2:
                # forth qdar
                show_text(f"section 4",175, (150,100,20))
                move_xy = [(screen_w//2) + min_len,(screen_h//2) +  min_len] # done

        elif snap and ((screen_w//2)-(snap_dis//2) <= xy[0] <= (screen_w//2)+(snap_dis//2)):
            move_xy[0] = screen_w//2
            draw = True
            
        elif snap and ((screen_h//2)-(snap_dis//2) <= xy[1] <= (screen_h//2)+(snap_dis//2)):
            move_xy[1] = screen_h//2
            draw = True

        else:
            draw = False

    else:
        # print("Y/B",(yellow_line_len / blue_line_len)%10,"B/Y", (blue_line_len / yellow_line_len)%10)

        # returning_speedX = round((yellow_line_len / blue_line_len)%10,3)
        # returning_speedY = round((blue_line_len / yellow_line_len)%10,3)

        # retract to origin
        if move_xy[0] > screen_c[0]:
            move_xy[0] -= returning_speedX
        elif move_xy[0] < screen_c[0]:
            move_xy[0] += returning_speedX

        if move_xy[1] > screen_c[1]:
            move_xy[1] -= returning_speedY
        elif move_xy[1] < screen_c[1]:
            move_xy[1] += returning_speedY
        

    pygame.draw.line(screen, (255, 255, 0), (screen_w//2,move_xy[1]), move_xy, 3) # yellow line touching red aixs
    pygame.draw.line(screen, (0, 0, 255), (move_xy[0],screen_h//2), move_xy, 3) # blue line touching green aixs
    
    pygame.draw.circle(screen, (255,255,255), move_xy,60, 2)

    if draw and pygame.mouse.get_focused():
        line = pygame.draw.line(screen, (255, 255, 255), screen_c, move_xy, 3)

    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)

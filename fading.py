import pygame

pygame.init()

clock = pygame.time.Clock()
FPS = 30

screen_w, screen_h = 500, 500
screen = pygame.display.set_mode((screen_w, screen_h))

def step(x):
    return int(x * (1.5 + (x/1000)))

def fade():
    global alpha
    fading = False
    r = 300
    inc = 10
    animate_rect = 0

    fade_in = 1

    surf = pygame.Surface((300, 300))
    rect = pygame.draw.rect(surf, "red", pygame.Rect(50, 50, 200, 200))
    surf.set_alpha(0)

    while True:

        screen.fill((100, 100, 100))

        if fading:
            if alpha < r and fade_in == 1:
                alpha += inc
                surf.set_alpha(alpha)
                animate_rect = pygame.Rect((100,screen_h-step(alpha)),surf.get_size())
            elif alpha >= 0:
                fade_in = 0
                alpha -= inc
                surf.set_alpha(alpha)
                animate_rect = pygame.Rect((100,screen_h-step(alpha)),surf.get_size())
            if alpha <= 0:
                fading = False
                print(surf.get_alpha())

        if surf.get_alpha() > inc:
            screen.blit(surf, animate_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not fading:
                    print("pressed")
                    alpha = 0
                    fading = True
                    fade_in = 1

        clock.tick(FPS)
        pygame.display.update()


if __name__ == "__main__":
    fade()

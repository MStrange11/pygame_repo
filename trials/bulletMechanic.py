import pygame
import sys

import warnings

warnings.filterwarnings("ignore")


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # self.image = pygame.Surface((100, 100))
        # self.image.fill((255, 255, 255))

        self.image = pygame.transform.scale(pygame.image.load("code material\\ship2.png"), (100, 100))

        self.rect = self.image.get_rect(center=(screen_width / 2, screen_height / 2))

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

    def create_bullet(self):
        return Bullet(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        # self.image = pygame.Surface((10, 50))
        # self.image.fill((255, 0, 0))

        self.image = pygame.transform.scale(pygame.image.load("code material\\bullet.png"), (50, 100))
        self.rect = self.image.get_rect(center=(pos_x, pos_y))

    def update(self):
        global bullet_count
        self.rect.y -= 10

        if self.rect.y <= 0 - 50:
            self.kill()
            bullet_count += 1
            print("bullet destroyed", bullet_count)


# Basics
pygame.init()
clock = pygame.time.Clock()
screen_width, screen_height = 800, 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.mouse.set_visible(False)

player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)

bullet_group = pygame.sprite.Group()
bullet_count = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Fix the event type here
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            bullet_group.add(player.create_bullet())

    screen.fill((50, 200, 50))
    bullet_group.draw(screen)
    player_group.draw(screen)
    bullet_group.update()
    player_group.update()
    pygame.display.flip()
    clock.tick(60)

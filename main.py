import pygame
import sys

from screen import win, W, H
from playerANDgun import Player, Gun
from mapLoader import map_controller

pygame.init()

egg = Player(W, H)
gun = Gun(W, H)

player_group = pygame.sprite.Group()
player_group.add(egg)
player_group.add(gun)


def functionality():
    egg.rotate()
    gun.rotate(egg.angle)

    egg.move()
    gun.move()


def sprite_drawer():
    player_group.update(win)


def map_drawer():
    win.fill((255, 255, 255))
    map_controller(win)


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                gun.shot()
                egg.shot()

        functionality()

        map_drawer()
        sprite_drawer()
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()

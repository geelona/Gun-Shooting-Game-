import pygame
import sys
from screen import win, W, H

from playerANDgun import Player, Gun

pygame.init()

egg = Player(W, H)
gun = Gun(W, H)

player_group = pygame.sprite.Group()
player_group.add(egg)
player_group.add(gun)


def functionality():
    egg.rotate()
    gun.rotate(egg.angle)


def draw():
    win.fill((255, 255, 255))
    player_group.update(win)
    pygame.display.update()


def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        functionality()
        draw()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()

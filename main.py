import math

import pygame
import sys

from screen import win, W, H
from playerANDgun import Player, Gun, player_size
from mapLoader import Map
from collisions import collide_detector

color = (255, 0, 0)

pygame.init()

egg = Player(W, H)
gun = Gun(W, H)

player_group = pygame.sprite.Group()
player_group.add(egg)
player_group.add(gun)

current_map = Map()


def functionality():
    global color
    egg.rotate()
    gun.rotate(egg.angle)

    egg.move()
    gun.move()

#collision--------------------------------------------------------------------------------------------------------------
    # collide = collide_detector(current_map.coordinates, egg.coordinates,
    #                            current_map.obstacles_mask, egg.player_image_mask, player_size)
    # if collide[0]:
    #     color = (0, 255, 0)
    #
    #     rad = math.atan2(egg.coordinates[1] - collide[1][1], egg.coordinates[0] - collide[1][0])
    #
    #     egg.coordinates[0] += math.cos(rad) * (egg.dx + 1) * 3
    #     egg.coordinates[1] += math.sin(rad) * (egg.dy + 1) * 3
    #     gun.coordinates[0] += math.cos(rad) * (egg.dx + 1) * 3
    #     gun.coordinates[1] += math.sin(rad) * (egg.dy + 1) * 3
    # else:
    #     color = (255, 0, 0)
#collision--------------------------------------------------------------------------------------------------------------


def sprite_drawer():
    player_group.update(win)


def map_drawer():
    win.fill(color)
    current_map.update(win)


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

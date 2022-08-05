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

#collision---------------------------------------------------------------------------------------------------------------------
    collide = collide_detector(current_map.coordinates, egg.coordinates,
                               current_map.obstacles_mask, egg.player_image_mask, player_size)

    after_shoot_collide = collide_detector(current_map.coordinates, [egg.coordinates[0] - egg.dx, egg.coordinates[1] - egg.dy],
                               current_map.obstacles_mask, egg.player_image_mask, player_size)

    gravity_collide = collide_detector(current_map.coordinates, [egg.coordinates[0], egg.coordinates[1] - 3],
                               current_map.obstacles_mask, egg.player_image_mask, player_size)

    if collide[0]:

        if after_shoot_collide[0]: egg.dx = 0  
        if after_shoot_collide[1]: egg.dy = 0
        if after_shoot_collide[0]: gun.dx = 0
        if after_shoot_collide[1]: gun.dy = 0
     
        rad = math.atan2(egg.coordinates[1] - collide[1][1], egg.coordinates[0] - collide[1][0])
     
        egg.coordinates[1] += math.sin(rad) + 3 if egg.dy < 0 else math.sin(rad) - 3
        gun.coordinates[1] += math.sin(rad) + 3 if gun.dy < 0 else math.sin(rad) - 3
        
        egg.coordinates[1] -= math.sin(rad)
        gun.coordinates[1] -= math.sin(rad)

        if gravity_collide[0] is False: egg.coordinates[1] += 3
        if gravity_collide[0] is False: gun.coordinates[1] += 3
#collision---------------------------------------------------------------------------------------------------------------------

    egg.move()
    gun.move()

def sprite_drawer():
    player_group.update(win)


def map_drawer():
    current_map.update(win)


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.quit:
                run = false

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

import pygame

pygame.init()


def collide_detector(obstacle_pos, player_pos, obstacle_mask, player_mask, player_size):
    offset = (player_pos[0] - player_size / 2 - obstacle_pos[0], player_pos[1] - player_size / 2 - obstacle_pos[1])

    result = obstacle_mask.overlap(player_mask, offset)
    if result:
        return True, result
    else:
        return False, None

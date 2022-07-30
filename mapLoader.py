import pygame

pygame.init()

info = pygame.display.Info()
W, H = info.current_w, info.current_h

bg1, obstacles1 = pygame.transform.scale(pygame.image.load("images/map/1/bg.png"), (W, H)),\
                  pygame.transform.scale(pygame.image.load("images/map/1/obstacles.png"), (W, H))

maps = {"1": [bg1, obstacles1]
        }

current_map = 1


def map_controller(win):
    win.blit(maps[f"{current_map}"][0], (0, 0))
    win.blit(maps[f"{current_map}"][1], (0, 0))

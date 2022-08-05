import pygame

pygame.init()

info = pygame.display.Info()
W, H = info.current_w, info.current_h

bg1, obstacles1 = pygame.transform.scale(pygame.image.load("images/map/1/bg.png").convert_alpha(), (W, H)),\
                  pygame.transform.scale(pygame.image.load("images/map/1/obstacles.png").convert_alpha(), (W, H))

maps = {"1": [bg1, obstacles1]
        }

current_map = 1


class Map(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.bg = maps[f"{current_map}"][0]
        self.obstacles = maps[f"{current_map}"][1]
        self.obstacles_mask = pygame.mask.from_surface(self.obstacles)
        self.coordinates = [0, 0]

    def update(self, win):
        win.blit(self.bg, self.coordinates)
        win.blit(self.obstacles, self.coordinates)

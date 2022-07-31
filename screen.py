import pygame

pygame.init()

info = pygame.display.Info()
W, H = info.current_w, info.current_h

win = pygame.display.set_mode((W, H), pygame.FULLSCREEN)
pygame.display.set_icon(pygame.image.load('images/shotgun.png').convert_alpha())
pygame.display.set_caption("Gun Shooting")

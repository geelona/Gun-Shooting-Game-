import pygame
import math

player_img = pygame.image.load('images/EvilUkrainianEgg.png')
player_img = pygame.transform.scale(player_img, (60, 60))

gun_img = pygame.image.load('images/shotgun.png')
gun_img = pygame.transform.scale(gun_img, (100, 100))


class Main(pygame.sprite.Sprite):

    def __init__(self, w, h):
        super().__init__()

        self.coordinates = (w // 2, h // 2)
        self.blit_coordinates = None
        self.angle = 0


class Player(Main):

    def __init__(self, w, h):
        super().__init__(w, h)
        self.image = player_img
        self.image_dummy = self.image

    def rotate(self):
        mx, my = pygame.mouse.get_pos()
        rad = math.atan2(mx - self.coordinates[0], my - self.coordinates[1])
        self.angle = math.degrees(rad)
        self.image_dummy = pygame.transform.rotate(self.image, self.angle)

    def update(self, win):
        win.blit(self.image_dummy, (self.coordinates[0] - self.image_dummy.get_width() // 2,
                                    self.coordinates[1] - self.image_dummy.get_height() // 2))


class Gun(Main):

    def __init__(self, w, h):
        super().__init__(w, h)
        self.image = gun_img
        self.image_dummy = self.image
        self.coordinates = (self.coordinates[0], self.coordinates[1])

    def rotate(self, angle):
        mx, my = pygame.mouse.get_pos()

        rad = math.atan2(my - self.coordinates[1], mx - self.coordinates[0])

        self.image_dummy = pygame.transform.rotate(self.image, angle - 90)
        
        self.blit_coordinates = (self.coordinates[0] + math.cos(rad) * 50, self.coordinates[1] + math.sin(rad) * 50)

    def update(self, win):
        win.blit(self.image_dummy, (self.coordinates[0] - self.image_dummy.get_width() // 2,
                                    self.coordinates[1] - self.image_dummy.get_height() // 2))

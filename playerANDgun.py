import pygame
import math

pygame.init()

player_size = 60
player_img = pygame.image.load('images/Egg.png').convert_alpha()
player_img.set_alpha(255)
player_img = pygame.transform.scale(player_img, (player_size, player_size))

gun_img = pygame.image.load('images/shotgun.png').convert_alpha()
gun_img.set_alpha(255)
gun_img = pygame.transform.scale(gun_img, (100, 100))


class Main(pygame.sprite.Sprite):

    def __init__(self, w, h):
        super().__init__()

        self.w = w
        self.h = h

        self.coordinates = [w // 2, h // 2]
        self.blit_coordinates = None
        self.angle = 0

        self.dx = 0
        self.dy = 0

    def move(self):
        self.gravity()
        self.wall_intersection()
        self.shot_force()

    def gravity(self):
        self.coordinates = [self.coordinates[0], self.coordinates[1] + 3]

    def wall_intersection(self):
        if self.coordinates[0] > self.w + 60:
            self.coordinates[0] = -60
        if self.coordinates[0] < -60:
            self.coordinates[0] = self.w + 60
        if self.coordinates[1] > self.h + 60:
            self.coordinates[1] = -60
        if self.coordinates[1] < -60:
            self.coordinates[1] = self.h + 60

    def shot_force(self):
        if self.dx > 0:
            self.coordinates[0] -= self.dx
        if self.dy > 0:
            self.coordinates[1] -= self.dy
            self.dy -= 0.1
        if self.dx > 0 >= self.dy:
            self.dx -= 0.05

        if self.dx < 0:
            self.coordinates[0] -= self.dx
        if self.dy < 0:
            self.coordinates[1] -= self.dy
            self.dy += 0.1
        if self.dx < 0 <= self.dy:
            self.dx += 0.05

    def shot(self):
        mx, my = pygame.mouse.get_pos()
        rad = math.atan2(my - self.coordinates[1], mx - self.coordinates[0])

        self.dx = math.cos(rad) * 8
        self.dy = math.sin(rad) * 8


class Player(Main):

    def __init__(self, w, h):
        super().__init__(w, h)
        self.image = player_img
        self.image_dummy = self.image
        self.player_image_mask = pygame.mask.from_surface(self.image)

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

    def rotate(self, angle):
        mx, my = pygame.mouse.get_pos()

        rad = math.atan2(my - self.coordinates[1], mx - self.coordinates[0])

        self.image_dummy = pygame.transform.rotate(self.image, angle - 90)
        
        self.blit_coordinates = (self.coordinates[0] + math.cos(rad) * 50, self.coordinates[1] + math.sin(rad) * 50)

    def update(self, win):
        win.blit(self.image_dummy, (self.blit_coordinates[0] - self.image_dummy.get_width() // 2,
                                    self.blit_coordinates[1] - self.image_dummy.get_height() // 2))

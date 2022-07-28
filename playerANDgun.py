import pygame, math

player_img = pygame.image.load('images/EvilUkrainianEgg.png')
player_img = pygame.transform.scale(player_img, (60, 60))

gun_img = pygame.image.load('images/shotgun.png')
gun_img = pygame.transform.scale(gun_img, (100, 100))

class Main(pygame.sprite.Sprite):

    def __init__(self, W, H):
        super().__init__()

        self.coords = (W // 2, H // 2)
        self.angle = 0

class Player(Main):

    def __init__(self, W, H):
        super().__init__(W, H)
        self.image = player_img
        self.image_dummy = self.image

    def rotate(self):
        mx, my = pygame.mouse.get_pos()
        rad = math.atan2(mx - self.coords[0], my - self.coords[1])
        self.angle = math.degrees(rad)
        self.image_dummy = pygame.transform.rotate(self.image, self.angle)

    def update(self, win):
        win.blit(self.image_dummy, (self.coords[0] - self.image_dummy.get_width() // 2, self.coords[1] - self.image_dummy.get_height() // 2))

class Gun(Main):

    def __init__(self, W, H):
        super().__init__(W, H)
        self.image = gun_img
        self.image_dummy = self.image
        self.coords = (self.coords[0], self.coords[1])

    def rotate(self, angle):
        self.angle = angle - 90
        self.image_dummy = pygame.transform.rotate(self.image, self.angle)

    def update(self, win):
        win.blit(self.image_dummy, (self.coords[0] - self.image_dummy.get_width() // 2, self.coords[1] - self.image_dummy.get_height() // 2))



import pygame, math

player_img = pygame.image.load('images/EvilUkrainianEgg.png')
player_img = pygame.transform.scale(player_img, (60, 60))

class Player(pygame.sprite.Sprite):
    def __init__(self, W, H):
        super().__init__()

        self.image = player_img

        self.image_dummy = self.image

        self.coords = (W // 2, H // 2)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        self.angle = 0

    def rotate(self):
        mx, my = pygame.mouse.get_pos()
        
        rad = math.atan2(mx - self.coords[0], my - self.coords[1])
        self.angle = math.degrees(rad)

        self.image_dummy = pygame.transform.rotate(self.image, self.angle)

    def update(self, win):
        win.blit(self.image_dummy, self.coords)

import pygame, sys
from screen import win, W, H

pygame.init


def draw():
    win.fill((255, 255, 255))
    pygame.display.update()


def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()

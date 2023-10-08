import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join

WIDTH, HEIGHT = 512, 512

pygame.init()


class Text(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, text, font):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = font

    def draw(self, window):
        text = self.font.render(self.text, True, (0, 0, 0))
        window.blit(text, (self.rect.x, self.rect.y))
        pygame.display.update()

def main():
    pygame.init()
    pygame.display.set_caption("Platformer")
    window = pygame.display.set_mode((WIDTH, HEIGHT))

    run = True
    while run:
        # quit if needed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        window.fill((5, 255, 255))
        txt = Text(0, 0, 100, 100, "Hello", pygame.font.SysFont("Arial", 16))
        txt.draw(window)

    pygame.quit()


main()

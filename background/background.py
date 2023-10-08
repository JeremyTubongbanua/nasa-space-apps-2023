import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join

WIDTH, HEIGHT = 500, 500

pygame.init()


class Tile(pygame.sprite.Sprite):
    COLOR = (255, 0, 0)
    IMAGE = pygame.image.load(os.path.join("Blue.png"))

    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, window):
        window.blit(self.IMAGE, (self.rect.x, self.rect.y))


def draw_window(window, tiles):
    window.fill((255, 255, 255))
    for tile in tiles:
        tile.draw(window)
    pygame.display.update()

def init_tiles():
    TILE_WIDTH = 32
    TILE_HEIGHT = 32
    tiles = []
    for i in range(0, WIDTH, TILE_WIDTH):
        for j in range(0, HEIGHT, TILE_HEIGHT):
            tiles.append(Tile(i, j, TILE_WIDTH, TILE_HEIGHT))
    return tiles

def main():
    pygame.init()
    pygame.display.set_caption("Platformer")
    window = pygame.display.set_mode((WIDTH, HEIGHT))

    run = True

    tiles = init_tiles()

    while run:
        # quit if needed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.KEYDOWN:
                for tile in tiles:
                    tile.rect.y += 32
                    if tile.rect.y > HEIGHT:
                        tile.rect.y = -tile.rect.height
        # draw
        draw_window(window, tiles)

    pygame.quit()


main()

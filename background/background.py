import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join

WIDTH, HEIGHT = 512, 512

pygame.init()


class Tile(pygame.sprite.Sprite):
    COLOR = (255, 0, 0)
    IMAGE = pygame.image.load(os.path.join("Blue.png"))

    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, window):
        window.blit(self.IMAGE, (self.rect.x, self.rect.y))

    def tick(self):
        self.rect.y += 1
        if self.rect.y+self.rect.height > HEIGHT:
            self.rect.y = -self.rect.height

def init_tiles():
    TILE_WIDTH = 16
    TILE_HEIGHT = 16
    tiles = []
    for i in range(0, WIDTH, TILE_WIDTH):
        for j in range(0, HEIGHT, TILE_HEIGHT):
            tiles.append(Tile(i, j, TILE_WIDTH, TILE_HEIGHT))
    return tiles

def draw_tiles_background(window, tiles):
    window.fill((255, 255, 255))
    for tile in tiles:
        tile.draw(window)
    pygame.display.update()

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

        # happens every ticc:
        for tile in tiles:
            tile.tick()


        # draw tiles
        draw_tiles_background(window, tiles)

    pygame.quit()


main()

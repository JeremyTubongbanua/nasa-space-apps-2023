import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join
from sprites.tile import Tile, init_tiles
from sprites.text import Text


def draw_tiles_background(window, tiles):
    window.fill((255, 255, 255))
    for tile in tiles:
        tile.draw(window)


def main():
    WIDTH, HEIGHT = 512, 512

    pygame.init()
    pygame.display.set_caption("Platformer")

    window = pygame.display.set_mode((WIDTH, HEIGHT))

    tiles = init_tiles(WIDTH, HEIGHT) # for background
    text = Text(0, 0, "Hello World!", "Arial", 32, (0, 0, 0))

    run = True
    while run:
        # quit if needed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        # happens every tick:
        for tile in tiles:
            tile.tick(HEIGHT)

        # draw tiles
        draw_tiles_background(window, tiles)
        text.draw(window)
        pygame.display.update()

    pygame.quit()


main()

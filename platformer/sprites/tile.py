
import pygame
import os

def init_tiles(window_width, window_height):
    TILE_WIDTH = 16
    TILE_HEIGHT = 16
    tiles = []
    for i in range(0, window_width, TILE_WIDTH):
        for j in range(0, window_height, TILE_HEIGHT):
            tiles.append(Tile(i, j, TILE_WIDTH, TILE_HEIGHT))
    return tiles

class Tile(pygame.sprite.Sprite):
    COLOR = (255, 0, 0)
    IMAGE = pygame.image.load(os.path.join("assets", "Background", "Blue.png"))

    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, window):
        window.blit(self.IMAGE, (self.rect.x, self.rect.y))

    def tick(self, height):
        self.rect.y += 1
        if self.rect.y+self.rect.height > height:
            self.rect.y = -self.rect.height
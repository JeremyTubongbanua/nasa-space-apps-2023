import pygame

BASE_IMG_PATH = 'Pygame_tut/assets'

def load_image(path):
    # .convert makes image more optimal for pygame
    img = pygame.load_image(BASE_IMG_PATH + path).convert()
    img.set_colorkey ((0,0,0))
    return img
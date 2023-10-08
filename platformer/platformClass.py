import pygame

class Platform():
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (0, 0, 255)  # Change the color as needed

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)


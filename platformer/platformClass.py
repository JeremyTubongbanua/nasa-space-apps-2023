import pygame

class Platform():
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (0, 0, 255)  # Change the color as needed
        self.image = pygame.image.load('assets/cobble.png')
        # scale image down
        self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))


    def tick(self):
        self.rect.y = self.rect.y + 1

    def draw(self, window):
        # pygame.draw.rect(window, self.color, self.rect)
        window.blit(self.image, (self.rect.x, self.rect.y))


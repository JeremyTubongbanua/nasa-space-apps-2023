
import pygame

class Text(pygame.sprite.Sprite):
    def __init__(self, x, y, text, font_name, font_size, color):
        super().__init__()
        self.text = text
        self.x = x
        self.y = y
        self.font_name = font_name
        self.font_size = font_size
        self.font = pygame.font.SysFont(font_name, font_size)
        self.color = color
        self.frequency = 100
        self.counter = self.frequency


    def draw(self, window):
        window.blit(self.font.render(self.text, True, self.color), (self.x, self.y))

    def tick(self, text):
        if (self.counter < self.frequency):
            self.counter = self.counter + 1
            return
        self.counter = 0
        self.text = text

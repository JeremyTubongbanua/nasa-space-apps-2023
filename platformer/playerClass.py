import pygame

class Player():

    def __init__(self, x, y, width, height):
        super().__init__()

        # Position
        self.x = x
        self.y = y

        # Dimensions
        self.width = width
        self.height = height

        # Velocity
        self.velX = 0
        self.velY = 0

        # Create a rect attribute to represent the player's position and dimensions
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        # Keys pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        # Speed (you need to define this)
        self.speed = 4
        
        # Jumping stuff
        self.jumpVelocity = -15
        self.canJump = True

    def tick(self):
        # Update internal state, check for input, etc.
        self.inputMovement()

    def draw(self, window):
        # Draw the player to the window
        pygame.draw.rect(window, (123, 123, 12), self.rect)

    def inputMovement(self):
        self.velX = 0
        self.velY = 0
        if self.left_pressed and not self.right_pressed:
            self.velX = -self.speed
        if self.right_pressed and not self.left_pressed:
            self.velX = self.speed
        if self.up_pressed and not self.down_pressed and self.canJump:
            self.velY = -self.speed
        if self.down_pressed and not self.up_pressed:
            self.velY = self.speed

        self.x += self.velX
        self.y += self.velY

        # Update the rect to reflect the new position
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
    
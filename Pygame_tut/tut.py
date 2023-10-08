import sys

import pygame

from scripts.utils import load_image
from scripts.entities import PhysicsEntity


class Game:
    def __init__(self):
        # creating a the game window/screen 
        self.screen = pygame.display.set_mode((400,780))
        pygame.display.set_caption('Team Wesley: THE Game')

        # changing top left icon
        logo = pygame.image.load('Pygame_tut/assets/wesBack.jpeg')
        pygame.display.set_icon(logo)

        # clock -> fps
        self.clock = pygame.time.Clock()

        # # playermodel image
        # self.img = pygame.image.load('Pygame_tut/assets/player.png')
        # # removes all color from the image matchine the code
        # self.img.set_colorkey((0,0,0))

        # self.img_pos = [150, 260]
        
        self.movement = [False,False]
        
        self.assets = {
            'player': load_image('player.png')
        }
        
        #! Collision -> when you run into a "rectangle" -> causes something to happen
        self.collision_area = pygame.Rect(50,50,300, 50)
        
        #! Player
        self.player = PhysicsEntity(self, 'Player', (50,50), (8,15))



    def run(self):
        #! infinite loop for updating our game
        while True:

            # filling up the screen with a blue color to overwrite old instances of blit/image
            self.screen.fill((14,219,248))           
                
            #! PLAYER ENTITY STUFF
            self.player.update((self.movement[1] - self.movement[0], 0))
            self.player.render(self.screen)
            
            
            # #! Playermodel stuff
            # # changing the image position when pressing keys
            # self.img_pos[1] += (self.movement[1] - self.movement[0]) * 5

            # #relative to top left
            # # blit basically makes a collage onto another image
            # # screen is blitting an img onto itself with the position
            # self.screen.blit(self.img, self.img_pos)

            
            # handling events
            for event in pygame.event.get():
                # event for leaving/closing the window/app
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False
                
                        
            
            pygame.display.update()
            # forces the loop to run at 60fps
            self.clock.tick(60)
            
            
            # #! Collision
            # # Creates a rectangle with the dimensions of the shape
            # # top left position image (imp_pos[0], img_pos[1])
            # # width and height of rectangle
            # img_r = pygame.Rect(self.img_pos[0], self.img_pos[1], self.img.get_width(), self.img.get_height())
            
            # # Checking collision
            # if img_r.colliderect(self.collision_area):
            #     pygame.draw.rect(self.screen, (0,100,255), self.collision_area)
            # else:
            #     pygame.draw.rect(self.screen, (0,100,211), self.collision_area)

        

Game().run()

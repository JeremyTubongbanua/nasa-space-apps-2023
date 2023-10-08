import pygame
from sprites.tile import Tile, init_tiles
from sprites.text import Text

def draw_tiles_background(window, tiles):
    window.fill((255, 255, 255))
    for tile in tiles:
        tile.draw(window)

def draw_water_level(window, text):
    text.draw(window)

def main():
    # constants
    WIDTH, HEIGHT = 512, 512

    # init pygame stuff
    pygame.init()
    pygame.display.set_caption("Platformer")

    # init window
    window = pygame.display.set_mode((WIDTH, HEIGHT))

    # init stuff needed for game
    tiles = init_tiles(WIDTH, HEIGHT) # for background
    text = Text(0, 0, "0 mm", "Arial", 32, (0, 0, 0))
    current_water_level = 0

    # main game loop
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(60)
        # quit if needed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        # happens every tick:
        for tile in tiles:
            tile.tick(HEIGHT)

        if text.counter >= text.frequency:
            current_water_level = current_water_level + 1
        text.tick(str(current_water_level) + ' mm')

        # draw everything
        draw_tiles_background(window, tiles)
        draw_water_level(window, text)
        pygame.display.update()

    pygame.quit()

main()

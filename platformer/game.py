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
    tiles = init_tiles(WIDTH, HEIGHT)  # for background
    text = Text(0, 0, "0 mm", "Arial", 32, (0, 0, 0))
    water_levels = [-34.50405405, -30.60405405, -28.03810811, -25.76111111, -21.60594595, -23.74108108, -20.23648649, -16.60702703, -11.15648649, -7.06583333, -3.76675676, -1.62756757, 3.01405405, 4.375, 5.02405405, 7.33194444, 12.43486486, 13.66162162, 12.94459459, 24.01162162, 26.30918919, 30.09111111, 40.91054054, 43.19648649, 44.29756757, 48.46594595, 55.61216216, 56.41333333, 60.87351351, 63.81189189, 64.498]
    current_water_level_index = 0
    current_water_level = water_levels[current_water_level_index]

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

        text.tick(str(current_water_level) + ' mm')
        if text.counter >= text.frequency:
            current_water_level_index = current_water_level_index + 1
            current_water_level = water_levels[current_water_level_index]

        # draw everything
        draw_tiles_background(window, tiles)
        draw_water_level(window, text)
        pygame.display.update()

    pygame.quit()


main()

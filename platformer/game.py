import pygame
from sprites.tile import Tile, init_tiles
from sprites.text import Text
from playerClass import Player
from platformClass import Platform
import random


def draw_tiles_background(window, tiles):
    window.fill((255, 255, 255))
    for tile in tiles:
        tile.draw(window)


def draw_water_level(window, text):
    text.draw(window)


def main():
    # constants
    WIDTH, HEIGHT = 513, 513

    # init pygame stuff
    pygame.init()
    pygame.display.set_caption("Platformer")

    # init window
    window = pygame.display.set_mode((WIDTH, HEIGHT))

    # init stuff needed for game
    tiles = init_tiles(WIDTH, HEIGHT)  # for background
    text = Text(0, 0, "0 mm", "Arial", 32, (0, 0, 0))
    text2 = Text(0, 200, "1993", "Arial", 32, (0, 0, 0))
    water_levels = [-34.50405405, -30.60405405, -28.03810811, -25.76111111, -21.60594595, -23.74108108, -20.23648649, -16.60702703, -11.15648649, -7.06583333, -3.76675676, -1.62756757, 3.01405405, 4.375, 5.02405405,
                    7.33194444, 12.43486486, 13.66162162, 12.94459459, 24.01162162, 26.30918919, 30.09111111, 40.91054054, 43.19648649, 44.29756757, 48.46594595, 55.61216216, 56.41333333, 60.87351351, 63.81189189, 64.498]
    years = []
    for i in range(len(water_levels)):
        years.append(1993 + i)
    current_year_index = 0
    current_water_level_index = 0
    current_water_level = water_levels[current_water_level_index] + 34.5

    # platforms
    # (count, x)
    platforms_t = [
        (100, random.randint(0, HEIGHT)),
        (100, random.randint(0, HEIGHT)),
        (100, random.randint(0, HEIGHT)),
        (100, random.randint(0, HEIGHT)),
        (100, random.randint(0, HEIGHT)),
        (100, random.randint(0, HEIGHT)),
        (200, random.randint(0, HEIGHT)),
        (200, random.randint(0, HEIGHT)),
        (200, random.randint(0, HEIGHT)),
        (200, random.randint(0, HEIGHT)),
        (200, random.randint(0, HEIGHT)),
        (200, random.randint(0, HEIGHT)),
        (310, random.randint(0, HEIGHT)),
        (320, random.randint(0, HEIGHT)),
        (410, random.randint(0, HEIGHT)),
        (420, random.randint(0, HEIGHT)),
        (410, random.randint(0, HEIGHT)),
        (420, random.randint(0, HEIGHT)),
        (410, random.randint(0, HEIGHT)),
        (420, random.randint(0, HEIGHT)),
        (410, random.randint(0, HEIGHT)),
        (520, random.randint(0, HEIGHT)),
        (520, random.randint(0, HEIGHT)),
        (520, random.randint(0, HEIGHT)),
        (620, random.randint(0, HEIGHT)),
        (620, random.randint(0, HEIGHT)),
        (620, random.randint(0, HEIGHT)),
        (620, random.randint(0, HEIGHT)),
        (620, random.randint(0, HEIGHT)),
        (620, random.randint(0, HEIGHT)),
        (720, random.randint(0, HEIGHT)),
        (720, random.randint(0, HEIGHT)),
        (720, random.randint(0, HEIGHT)),
        (800, random.randint(0, HEIGHT)),
        (820, random.randint(0, HEIGHT)),
        (820, random.randint(0, HEIGHT)),
        (820, random.randint(0, HEIGHT)),
        (850, random.randint(0, HEIGHT)),
        (900, random.randint(0, HEIGHT)),
        (920, random.randint(0, HEIGHT)),
        (920, random.randint(0, HEIGHT)),
        (920, random.randint(0, HEIGHT)),
        (920, random.randint(0, HEIGHT)),
        (1000, random.randint(0, HEIGHT)),
        (1000, random.randint(0, HEIGHT)),
        (1100, random.randint(0, HEIGHT)),
        (1100, random.randint(0, HEIGHT)),
        (1200, random.randint(0, HEIGHT)),
        (1200, random.randint(0, HEIGHT)),
        (1000, random.randint(0, HEIGHT)),
        (1000, random.randint(0, HEIGHT)),
        (1100, random.randint(0, HEIGHT)),
        (1100, random.randint(0, HEIGHT)),
        (1200, random.randint(0, HEIGHT)),
        (1200, random.randint(0, HEIGHT)),
        (1300, random.randint(0, HEIGHT)),
        (1400, random.randint(0, HEIGHT)),
        (1500, random.randint(0, HEIGHT)),
        (1600, random.randint(0, HEIGHT)),
        (1700, random.randint(0, HEIGHT)),
        (1800, random.randint(0, HEIGHT)),
        (1900, random.randint(0, HEIGHT)),
        (2000, random.randint(0, HEIGHT)),
        (2000, random.randint(0, HEIGHT)),
        (2000, random.randint(0, HEIGHT)),
        (2000, random.randint(0, HEIGHT)),
        (2000, random.randint(0, HEIGHT)),
        (2000, random.randint(0, HEIGHT)),
        (2100, random.randint(0, HEIGHT)),
        (2100, random.randint(0, HEIGHT)),
        (2100, random.randint(0, HEIGHT)),
        (2100, random.randint(0, HEIGHT)),
        (2100, random.randint(0, HEIGHT)),
        (2100, random.randint(0, HEIGHT)),
        (2100, random.randint(0, HEIGHT)),
        (2200, random.randint(0, HEIGHT)),
        (2300, random.randint(0, HEIGHT)),
        (2300, random.randint(0, HEIGHT)),
        (2300, random.randint(0, HEIGHT)),
        (2300, random.randint(0, HEIGHT)),
        (2300, random.randint(0, HEIGHT)),
        (2300, random.randint(0, HEIGHT)),
        (2400, random.randint(0, HEIGHT)),
        (2500, random.randint(0, HEIGHT)),
        (2500, random.randint(0, HEIGHT)),
        (2500, random.randint(0, HEIGHT)),
        (2500, random.randint(0, HEIGHT)),
        (2500, random.randint(0, HEIGHT)),
        (2500, random.randint(0, HEIGHT)),
        (2500, random.randint(0, HEIGHT)),
        (2500, random.randint(0, HEIGHT)),
        (2600, random.randint(0, HEIGHT)),
        (2600, random.randint(0, HEIGHT)),
        (2600, random.randint(0, HEIGHT)),
        (2600, random.randint(0, HEIGHT)),
        (2600, random.randint(0, HEIGHT)),
        (2600, random.randint(0, HEIGHT)),
        (2600, random.randint(0, HEIGHT)),
        (2600, random.randint(0, HEIGHT)),
        (2600, random.randint(0, HEIGHT)),
        (2600, random.randint(0, HEIGHT)),
        (2600, random.randint(0, HEIGHT)),
        (2600, random.randint(0, HEIGHT)),
        (2600, random.randint(0, HEIGHT)),
        (2600, random.randint(0, HEIGHT)),
        (2600, random.randint(0, HEIGHT)),
        (2700, random.randint(0, HEIGHT)),
        (2700, random.randint(0, HEIGHT)),
        (2700, random.randint(0, HEIGHT)),
        (2700, random.randint(0, HEIGHT)),
        (2700, random.randint(0, HEIGHT)),
        (2700, random.randint(0, HEIGHT)),
        (2700, random.randint(0, HEIGHT)),
        (2700, random.randint(0, HEIGHT)),
        (2700, random.randint(0, HEIGHT)),
        (2700, random.randint(0, HEIGHT)),
        (2800, random.randint(0, HEIGHT)),
        (2800, random.randint(0, HEIGHT)),
        (2800, random.randint(0, HEIGHT)),
        (2800, random.randint(0, HEIGHT)),
        (2800, random.randint(0, HEIGHT)),
        (2800, random.randint(0, HEIGHT)),
        (2800, random.randint(0, HEIGHT)),
        (2800, random.randint(0, HEIGHT)),
        (2800, random.randint(0, HEIGHT)),
        (2800, random.randint(0, HEIGHT)),
        (2800, random.randint(0, HEIGHT)),
        (2900, random.randint(0, HEIGHT)),
        (3000, random.randint(0, HEIGHT)),
        (3000, random.randint(0, HEIGHT)),
        (3000, random.randint(0, HEIGHT)),
        (3000, random.randint(0, HEIGHT)),
        (3000, random.randint(0, HEIGHT)),
        (3000, random.randint(0, HEIGHT)),
        (3000, random.randint(0, HEIGHT)),
        (3000, random.randint(0, HEIGHT)),
        (3000, random.randint(0, HEIGHT)),
        (3000, random.randint(0, HEIGHT)),
        (3000, random.randint(0, HEIGHT)),
        (3000, random.randint(0, HEIGHT)),
        (3100, random.randint(0, HEIGHT)),
        (3100, random.randint(0, HEIGHT)),
        (3100, random.randint(0, HEIGHT)),
        (3100, random.randint(0, HEIGHT)),
        (3100, random.randint(0, HEIGHT)),
        (3100, random.randint(0, HEIGHT)),
        (3100, random.randint(0, HEIGHT)),
        (3100, random.randint(0, HEIGHT)),
        (3100, random.randint(0, HEIGHT)),
        (3200, random.randint(0, HEIGHT)),
        (3200, random.randint(0, HEIGHT)),
        (3200, random.randint(0, HEIGHT)),
        (3200, random.randint(0, HEIGHT)),
        (3200, random.randint(0, HEIGHT)),
        (3200, random.randint(0, HEIGHT)),
        (3200, random.randint(0, HEIGHT)),
        (3200, random.randint(0, HEIGHT)),
        (3200, random.randint(0, HEIGHT)),
        (3200, random.randint(0, HEIGHT)),
        (3300, random.randint(0, HEIGHT)),
        (3300, random.randint(0, HEIGHT)),
        (3300, random.randint(0, HEIGHT)),
        (3300, random.randint(0, HEIGHT)),
        (3300, random.randint(0, HEIGHT)),
        (3300, random.randint(0, HEIGHT)),
        (3300, random.randint(0, HEIGHT)),
        (3300, random.randint(0, HEIGHT)),
        (3300, random.randint(0, HEIGHT)),
        (3300, random.randint(0, HEIGHT)),
        (3300, random.randint(0, HEIGHT)),
        (3300, random.randint(0, HEIGHT)),
        (3300, random.randint(0, HEIGHT)),
        (3300, random.randint(0, HEIGHT)),
        (3300, random.randint(0, HEIGHT)),
        (3400, random.randint(0, HEIGHT)),
        (3400, random.randint(0, HEIGHT)),
        (3400, random.randint(0, HEIGHT)),
        (3400, random.randint(0, HEIGHT)),
        (3400, random.randint(0, HEIGHT)),
        (3400, random.randint(0, HEIGHT)),
        (3400, random.randint(0, HEIGHT)),
        (3400, random.randint(0, HEIGHT)),
        (3400, random.randint(0, HEIGHT)),
        (3400, random.randint(0, HEIGHT)),
        (3400, random.randint(0, HEIGHT)),
        (3400, random.randint(0, HEIGHT)),
        (3400, random.randint(0, HEIGHT)),
        (3500, random.randint(0, HEIGHT)),
        (3500, random.randint(0, HEIGHT)),
        (3500, random.randint(0, HEIGHT)),
        (3500, random.randint(0, HEIGHT)),
        (3500, random.randint(0, HEIGHT)),
        (3500, random.randint(0, HEIGHT)),
        (3500, random.randint(0, HEIGHT)),
        (3500, random.randint(0, HEIGHT)),
        (3500, random.randint(0, HEIGHT)),
        (3500, random.randint(0, HEIGHT)),
        (3500, random.randint(0, HEIGHT)),
        (3500, random.randint(0, HEIGHT)),
        (3500, random.randint(0, HEIGHT)),
        (3500, random.randint(0, HEIGHT)),
        (3500, random.randint(0, HEIGHT)),
        (3500, random.randint(0, HEIGHT)),
        (3500, random.randint(0, HEIGHT)),
    ]
    platforms = []
    c = 0

    # init player
    player = Player(HEIGHT/2, WIDTH/2, 75, 75)

    # # init floor
    # floor = pygame.Rect(0, HEIGHT - 20, WIDTH, 20)

    # platforms = [Platform(0, HEIGHT - 20, WIDTH, 20)]

    # main game loop
    clock = pygame.time.Clock()
    run = True
    while run:

        c = c + 1

        # 60 fps
        clock.tick(60)

        # quit if needed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        # happens every tick:
        for tile in tiles:
            tile.tick(HEIGHT)

        t = 'GMSL: %.2f mm' % current_water_level
        text.tick(str(t))
        if text.counter >= text.frequency:
            current_water_level_index = current_water_level_index + 1
            if current_water_level_index >= len(water_levels):
                break
            current_water_level = water_levels[current_water_level_index] + 34

        print(str(years[current_water_level_index]))
        text2.tick(str(years[current_water_level_index]))

        # draw everything
        draw_tiles_background(window, tiles)
        draw_water_level(window, text)
        text2.draw(window)
        pygame.display.update()

        # Draw platforms
        print(c)
        for t in platforms_t:
            count, x = t
            if c == count:
                platform = Platform(x, 0, 50, 20)
                platforms.append(platform)

        for platform in platforms:
            platform.tick()

        for platform in platforms:
            platform.draw(window)

        for platform in platforms:
            if platform.rect.y > HEIGHT:
                platforms.remove(platform)

        player.draw(window)

        # Get the state of all keys (continuous input)
        keys = pygame.key.get_pressed()

        # Update player movement based on continuous key state
        player.left_pressed = keys[pygame.K_LEFT]
        player.right_pressed = keys[pygame.K_RIGHT]
        player.up_pressed = keys[pygame.K_UP]
        player.down_pressed = keys[pygame.K_DOWN]

        # Call the tick method of the player to update its state
        player.tick()

        # Draw the player
        player.draw(window)

        pygame.display.update()

    # window.fill((255, 255, 255))

    text = Text((WIDTH/2) - 100, (HEIGHT/2) - 100,
                "GAME OVER - You Won!", "Times New Roman", 32, (0, 255, 0))
    text.draw(window)

    pygame.display.update()

    pygame.time.delay(8*1000)

    pygame.quit()


main()

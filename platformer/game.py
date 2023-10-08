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
    WIDTH, HEIGHT = 800, 800

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
    current_water_level_index = 0
    current_water_level = water_levels[current_water_level_index]

    # platforms
    # (count, x)
    platforms_t = [
        (100, random.randint(0, 800)),
        (100, random.randint(0, 800)),
        (200, random.randint(0, 800)),
        (210, random.randint(0, 800)),
        (220, random.randint(0, 800)),
        (900, random.randint(0, 800)),
        (1000, random.randint(0, 800)),
        (1000, random.randint(0, 800)),
        (1100, random.randint(0, 800)),
        (1100, random.randint(0, 800)),
        (1200, random.randint(0, 800)),
        (1200, random.randint(0, 800)),
        (1300, random.randint(0, 800)),
        (1400, random.randint(0, 800)),
        (1500, random.randint(0, 800)),
        (1600, random.randint(0, 800)),
        (1700, random.randint(0, 800)),
        (1800, random.randint(0, 800)),
        (1900, random.randint(0, 800)),
        (2000, random.randint(0, 800)),
        (2100, random.randint(0, 800)),
        (2200, random.randint(0, 800)),
        (2300, random.randint(0, 800)),
        (2400, random.randint(0, 800)),
        (2500, random.randint(0, 800)),
        (2600, random.randint(0, 800)),
        (2700, random.randint(0, 800)),
        (2800, random.randint(0, 800)),
        (2900, random.randint(0, 800)),
        (3000, random.randint(0, 800)),
        (3100, random.randint(0, 800)),
        (3200, random.randint(0, 800)),
        (3300, random.randint(0, 800)),
        (3400, random.randint(0, 800)),
        (3500, random.randint(0, 800)),
    ]
    platforms = []
    c = 0

    # init player
    player = Player(HEIGHT/2, WIDTH/2, 25, 25)

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

        text.tick(str(current_water_level) + ' mm')
        if text.counter >= text.frequency:
            current_water_level_index = current_water_level_index + 1
            if current_water_level_index >= len(water_levels):
                break
            current_water_level = water_levels[current_water_level_index]

        text2.tick(str())

        # draw everything
        draw_tiles_background(window, tiles)
        draw_water_level(window, text)
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

    window.fill((255, 255, 255))

    text = Text(WIDTH/2, HEIGHT/2, "GAME OVER", "Arial", 32, (0, 0, 0))
    text.draw(window)

    pygame.display.update()

    pygame.time.delay(5000)

    pygame.quit()


main()

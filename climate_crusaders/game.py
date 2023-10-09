import pygame
import sys
import os
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
CRAB_WIDTH, CRAB_HEIGHT = 50, 50
GROUND_HEIGHT = 50
SKY_BLUE = (135, 206, 235)
GREEN = (0, 255, 0)
GRAVITY = 1
CRAB_SPEED = 5
BROWN = (139, 69, 19)
PLATFORM_WIDTH, PLATFORM_HEIGHT = CRAB_WIDTH * 2, CRAB_HEIGHT // 2
black_block = pygame.Rect(0, HEIGHT + 100, WIDTH, CRAB_HEIGHT)
black_block_speed = 0.6
black_block_acceleration = 0.005
timer = 1993
timer_array = list(range(1993, 2023))
water_levels = [-34.50405405, -30.60405405, -28.03810811, -25.76111111, -21.60594595, -23.74108108, -20.23648649, -16.60702703, -11.15648649, -7.06583333, -3.76675676, -1.62756757, 3.01405405, 4.375, 5.02405405,
                7.33194444, 12.43486486, 13.66162162, 12.94459459, 24.01162162, 26.30918919, 30.09111111, 40.91054054, 43.19648649, 44.29756757, 48.46594595, 55.61216216, 56.41333333, 60.87351351, 63.81189189, 64.498]

sand_block = pygame.Rect(0, 600 - 200, WIDTH, 200)
SAND_COLOR = (194, 178, 128)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

crab = pygame.Rect(WIDTH // 2, HEIGHT - CRAB_HEIGHT -
                   GROUND_HEIGHT, CRAB_WIDTH, CRAB_HEIGHT)
crab_y_speed = 0
jumping = False

# Set up the ground
ground = pygame.Rect(0, HEIGHT - GROUND_HEIGHT, WIDTH, GROUND_HEIGHT)

# Set up the platforms

platforms = [pygame.Rect(random.randint(0, WIDTH - PLATFORM_WIDTH), HEIGHT - (
    i+2) * 50 - GROUND_HEIGHT, PLATFORM_WIDTH, PLATFORM_HEIGHT) for i in range(55)]

# Define start_button as a global variable
start_button = pygame.Rect(WIDTH//2 - 100, HEIGHT//2 - 200, 200, 50)


def draw_menu():
    
    screen.fill(SKY_BLUE)  # Fill the screen with sky blue

    font = pygame.font.Font(None, 74)

    pygame.draw.rect(screen, GREEN, start_button)

    font = pygame.font.Font(None, 50)
    text = font.render("Start", 1, (0, 0, 0))
    screen.blit(text, (WIDTH//2 - 50, HEIGHT//2 - 190))
    climate_crusaders_image = pygame.image.load(
        os.path.join("assets", "FinalTitle.png"))
    screen.blit(climate_crusaders_image, (WIDTH//2 - climate_crusaders_image.get_width()//2, HEIGHT //
                2 + start_button.height//2 - climate_crusaders_image.get_height()//2))

    pygame.display.update()  # Update the display


def main_menu():
    in_menu = True
    while in_menu:
        draw_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # The user closed the window!
                pygame.quit()
                sys.exit()  # Terminate the script

            if event.type == pygame.MOUSEBUTTONDOWN:  # The user clicked the mouse!
                mouse_pos = pygame.mouse.get_pos()
                # The user clicked inside the start button!
                if start_button.collidepoint(mouse_pos):
                    in_menu = False


def draw_window():
    screen.fill(SKY_BLUE)  # Fill the screen with sky blue
    background_image = pygame.image.load(os.path.join("assets", "bac.jpg"))
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
    screen.blit(background_image, (0, 0))

    # Draw the timer
    font = pygame.font.Font(None, 50)
    text = font.render(str(timer), 1, (0, 0, 0))
    screen.blit(text, (10, 10))

    year_text = pygame.font.Font(None, 50)
    if(timer > 2023):
        return
    year_text_sprite = year_text.render(str(water_levels[timer-1993]), 1, (0, 0, 0))
    screen.blit(year_text_sprite, (10, 50))

    fixed_crab = pygame.Rect(crab.x, HEIGHT // 2, CRAB_WIDTH, CRAB_HEIGHT)
    # pygame.draw.rect(screen, GREEN, fixed_crab)
    crab_image = pygame.image.load(os.path.join("assets", "crab.png"))
    screen.blit(crab_image, fixed_crab)

    fixed_ground = pygame.Rect(
        ground.x, ground.y - crab.y + HEIGHT // 2, ground.width, ground.height)
    pygame.draw.rect(screen, GREEN, fixed_ground)

    for platform in platforms:
        fixed_platform = pygame.Rect(
            platform.x, platform.y - crab.y + HEIGHT // 2, platform.width, platform.height)
        pygame.draw.rect(screen, BROWN, fixed_platform)


    fixed_black_block = pygame.Rect(
        black_block.x, black_block.y - crab.y + HEIGHT // 2, black_block.width, black_block.height)
    # pygame.draw.rect(screen, (0, 105, 148), fixed_black_block)
    water_image = pygame.image.load(os.path.join("assets", "water.png"))
    water_image = pygame.transform.scale(water_image, (1000, 500))
    screen.blit(water_image, fixed_black_block)



    pygame.display.update()  # Update the display


def main():
    global crab_y_speed, jumping, timer, black_block_speed, black_block_acceleration

    clock = pygame.time.Clock()
    timer_event = pygame.USEREVENT + 1
    pygame.time.set_timer(timer_event, 1000)  # Timer event every second

    while True:
        clock.tick(60)  # Cap the frame rate at 60 FPS

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # The user closed the window!
                pygame.quit()
                sys.exit()  # Terminate the script

            if event.type == timer_event:  # Timer event occurred!
                timer += 1

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not jumping:  # The user pressed space!
                    crab_y_speed = -15
                    jumping = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:  # The 'w' key is being held down!
            crab.x -= CRAB_SPEED
        if keys[pygame.K_d]:  # The 'd' key is being held down!
            crab.x += CRAB_SPEED

        crab_y_speed += GRAVITY

        crab.y += crab_y_speed

        black_block_speed += black_block_acceleration

        # Move the black block upwards
        black_block.y -= black_block_speed

        # Check for collision with ground

        if crab.colliderect(ground):
            if crab_y_speed > 0:  # The crab is falling
                crab.y = ground.y - CRAB_HEIGHT

        # Check for collision with platforms

        for platform in platforms:
            if crab.colliderect(platform) and crab_y_speed > 0:  # The crab is falling
                crab.y = platform.y - CRAB_HEIGHT
                crab_y_speed = 0
                jumping = False


        if crab.colliderect(black_block):

            break

        draw_window()
    
    screen.blit(pygame.image.load(os.path.join("assets", "game-over.png")), (0, 0))
    pygame.display.update()
    pygame.time.delay(3000)


main_menu()
main()

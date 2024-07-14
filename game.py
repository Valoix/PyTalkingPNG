import pygame
import asyncio
import os
import random

def rotate_image(image, angle):
    return pygame.transform.rotate(image, angle)

def blinker():
    global time_until_blink
    if time_until_blink == 0:
        time_until_blink = random.randint(200, 400)
        return True
    else:
        time_until_blink -= 1
        return False

def run_game():
    global blink_timer
    global player_x,player_y
    global time_until_blink

    time_until_blink = random.randint(150, 400)

    # Set up the game window
    WINDOW_WIDTH = 1280
    WINDOW_HEIGHT = 720

    # Define colors
    BACKGROUND = (0, 255, 0)

    # Define player properties
    PLAYER_SIZE = 720
    player_x = WINDOW_WIDTH // 2 - PLAYER_SIZE /2
    player_y = WINDOW_HEIGHT // 2 - PLAYER_SIZE /2

    target_y = WINDOW_HEIGHT // 2 - PLAYER_SIZE /2

    normal_image = pygame.image.load("./assets/openeyes-closedmouth.png")
    normal_image = pygame.transform.scale(normal_image, (PLAYER_SIZE, PLAYER_SIZE))

    blink_image = pygame.image.load("./assets/closedeyes-closedmouth.png")
    blink_image = pygame.transform.scale(blink_image, (PLAYER_SIZE, PLAYER_SIZE))

    talking_normal_image = pygame.image.load("./assets/openeyes-openmouth.png")
    talking_normal_image = pygame.transform.scale(talking_normal_image, (PLAYER_SIZE, PLAYER_SIZE))

    talking_blink_image = pygame.image.load("./assets/closedeyes-openmouth.png")
    talking_blink_image = pygame.transform.scale(talking_blink_image, (PLAYER_SIZE, PLAYER_SIZE))

    # To allow the blink to stay closed
    blink_timer = 0
    
    # To allow the player to jump
    jump_velocity = 0
    GRAVITY = 2

    # For !rotate
    rotation_angle = 0
    is_rotating = False

    # For !shrink
    is_shrinking = False
    shrink_timer = 0
    current_scale = 1.0
    target_scale = 0.5

    # Initialize Pygame
    pygame.init()

    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Valoix's PNGTuber Application")
    clock = pygame.time.Clock()

    # Game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Read the contents of input.txt
        try:
            with open("input.txt", "r") as f:
                direction = f.read().strip()
        except FileNotFoundError:
            direction = None

        # Handle Chat Command Inputs
        # !rotate
        if direction == "rotate":
            is_rotating = True
        if is_rotating:
            rotation_angle += 10
            if rotation_angle > 360:
                rotation_angle = 0
                is_rotating = False
        
        # !shrink
        if direction == "shrink" and not is_shrinking:
            is_shrinking = True
            shrink_timer = 360  # 6 seconds at 60 FPS
        if is_shrinking:
            if shrink_timer > 270:  # First 1.5 seconds: shrink
                current_scale = max(target_scale, current_scale - 0.01)
                target_y = WINDOW_HEIGHT // 2 - PLAYER_SIZE /2 + (PLAYER_SIZE * (1 - current_scale) // 2)
            elif shrink_timer > 90:  # Next 3 seconds: stay at target scale
                pass
            elif shrink_timer > 0:  # Next 1.5 seconds: grow
                current_scale = min(1.0, current_scale + 0.01)
                target_y = WINDOW_HEIGHT // 2 - PLAYER_SIZE /2 + (PLAYER_SIZE * (1 - current_scale) // 2)
            else:  # Animation complete
                is_shrinking = False
                current_scale = 1.0
            shrink_timer -= 1
            

        # Clear the window
        window.fill(BACKGROUND)

        # Get the volume of the microphone
        with open("mic_volume.txt", "r") as f:
            volume = f.read()
            if volume == '':
                volume = 0
            else:
                volume = int(volume)
            f.close()
        # Determine if the player is talking
        if volume > 100:
            talking = True
        else:
            talking = False
            if player_y == target_y:
                jump_ready = True

        # Create physics for the model
        if talking and jump_ready:
            jump_velocity = -10
            jump_ready = False

        player_y += jump_velocity
        jump_velocity += GRAVITY

        if player_y > target_y:
            player_y = target_y
            jump_velocity = 0

        # Draw the player
        if talking:
            current_image = talking_normal_image if blink_timer == 0 else talking_blink_image
        else:
            current_image = normal_image if blink_timer == 0 else blink_image

        scaled_image = pygame.transform.scale(current_image, (int(PLAYER_SIZE * current_scale), int(PLAYER_SIZE * current_scale)))
        rotated_image = rotate_image(scaled_image, rotation_angle)
        rect = rotated_image.get_rect(center=(player_x + PLAYER_SIZE/2, player_y + PLAYER_SIZE/2))
        window.blit(rotated_image, rect)

        if blinker():
            blink_timer = random.randint(10, 40)
        if blink_timer > 0:
            blink_timer -= 1

        # Update the display
        pygame.display.update()
        clock.tick(60)
        
    # Quit Pygame
    pygame.quit()


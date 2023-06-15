import pygame
import sys
from random import randint

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
display = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Ball properties
ball_radius = 20
ball_color = (255, 0, 0)
ball_position = [width // 2, ball_radius]
ball_velocity = 0

# Engine properties
engine_power = 1
engine_active = False

# Gravity
gravity = 0.5

# Ground properties
ground_height = height - ball_radius

# Background image
background_image = pygame.image.load("gurocketry-school-outreach/stars.jpg").convert()
background_image = pygame.transform.scale(background_image, (800, 600))

# Rocket
rocket_image = pygame.image.load("gurocketry-school-outreach/rocket.png")
rocket_image = pygame.transform.scale(rocket_image, (150, 150))

# Flame
flame_image = pygame.image.load("gurocketry-school-outreach/flame.png")
flame_image = pygame.transform.scale(flame_image, (64, 64))

# Game loop
while True :
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                engine_active = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                engine_active = False

    # Update ball position
    ball_velocity += gravity

    if engine_active:
        ball_velocity -= engine_power

    ball_position[1] += ball_velocity

    # Check if ball hits the ground
    if ball_position[1] + ball_radius + 50 >= ground_height:
        if ball_velocity > 10:
            ball_color = (0, 255, 255)
        ball_position[1] = ground_height - ball_radius - 50
        ball_velocity = 0
        

    # Clear the display
    display.fill((0, 0, 0))

    # Set background image
    display.blit(background_image, [0, 0])
    

    # Draw the ball + rocket + flame
    pygame.draw.circle(display, ball_color, (int(ball_position[0]), int(ball_position[1])), ball_radius)
    display.blit(rocket_image, (int(ball_position[0]) - 75, int(ball_position[1]) -  80))
    if engine_active:
        display.blit(flame_image, (int(ball_position[0]) - 30 + randint(-2, 2), int(ball_position[1]) + 45 + randint(-2, 2)))

    # Draw the ground
    pygame.draw.rect(display, (200, 200, 200), (0, ground_height, width, height - ground_height))

    # Update the display
    pygame.display.flip()
    clock.tick(30)

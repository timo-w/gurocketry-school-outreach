import pygame
import sys
from random import randint




########################

# How long to wait until starting the landing burn
delay = 30
# How long the burn will last
duration = 20
# The power level of the engine
engine_power = 1

########################




# Initialize Pygame
pygame.init()

# Set up the display
width, height = 600, 800
display = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Ball properties
ball_radius = 20
ball_color = (255, 0, 0)
ball_position = [width // 2, ball_radius]
ball_velocity = 0

# Engine properties
engine_active = False
fuel = 100
time_elapsed = 0

# Game over
game_finished = False
game_end_state = ""
score = 0

# Gravity
gravity = 0.5

# Ground properties
ground_height = height - ball_radius

# Background image
background_image = pygame.image.load("gurocketry-school-outreach/stars.jpg").convert()
background_image = pygame.transform.scale(background_image, (800, 800))

# Rocket
rocket_image = pygame.image.load("gurocketry-school-outreach/rocket.png")
rocket_image = pygame.transform.scale(rocket_image, (150, 150))

# Flame
flame_image = pygame.image.load("gurocketry-school-outreach/flame.png")
flame_image = pygame.transform.scale(flame_image, (64, 64))

# Text
font = pygame.font.SysFont("Arial", 26)
txt_fuel = font.render("Fuel left: " + str(fuel), True, (255, 255, 255))
txt_time = font.render("Time elapsed: " + str(time_elapsed), True, (255, 255, 255))
txt_score = font.render("Score: " + str(score), True, (255, 255, 255))
txt_crashed = font.render("The rocket hit the surface too hard! Try again!", True, (255, 255, 255))
txt_success = font.render("Successful landing!", True, (255, 255, 255))

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Keep track of stats
    if delay > 0:
        delay -= 1
    else:
        if duration > 0:
            duration -= 1
            if fuel <= 0:
                engine_active = False
            else:
                fuel = round(fuel - engine_power, 2)
                engine_active = True
        else:
            engine_active = False

    # Increment time
    if not game_finished:
        time_elapsed += 1



    # Update ball position
    ball_velocity += gravity

    if engine_active:
        ball_velocity -= engine_power

    ball_position[1] += ball_velocity

    # Check if ball hits the ground
    if ball_position[1] + ball_radius + 50 >= ground_height:
        game_finished = True
        score = fuel + (1000 - time_elapsed)
        if ball_velocity > 5:
            game_end_state = "crashed"
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
    pygame.draw.rect(display, (200, 170, 160), (0, ground_height, width, height - ground_height))

    # Text
    if game_finished and game_end_state == "crashed":
        display.blit(txt_crashed,(300 - txt_crashed.get_width() // 2, 400 - txt_crashed.get_height() // 2))
    elif game_finished:
        display.blit(txt_success,(300 - txt_success.get_width() // 2, 400 - txt_success.get_height() // 2))
        txt_score = font.render("Score: " + str(score), True, (255, 255, 255))
        display.blit(txt_score,(300 - txt_score.get_width() // 2, 430 - txt_score.get_height() // 2))
    

    # Display fuel and time text
    txt_fuel = font.render("Fuel left: " + str(fuel), True, (255, 255, 255))
    txt_time = font.render("Time elapsed: " + str(time_elapsed), True, (255, 255, 255))
    display.blit(txt_fuel,(30, 100 - txt_fuel.get_height() // 2))
    display.blit(txt_time,(30, 60 - txt_time.get_height() // 2))
    

    # Update the display
    pygame.display.flip()
    clock.tick(30)


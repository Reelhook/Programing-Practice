import pygame
import sys
from pygame.math import Vector2

# Initialize the game engine
pygame.init()

# Set up the window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Push the Ball with Your Cursor")

clock = pygame.time.Clock()
FPS = 60

# Ball properties
ball_pos = Vector2(WIDTH / 2, HEIGHT / 2)
ball_vel = Vector2(0, 0)
ball_radius = 20
friction = 0.98  # Friction factor to slow the ball over time

# Variables to manage the pushing state
pushing = False
prev_mouse_pos = None

# Main game loop
while True:
    dt = clock.tick(FPS)  # Control the game's frame rate

    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Begin pushing if the mouse is inside the ball
            mouse_pos = Vector2(event.pos)
            if mouse_pos.distance_to(ball_pos) <= ball_radius:
                pushing = True
                prev_mouse_pos = mouse_pos

        elif event.type == pygame.MOUSEBUTTONUP:
            # Stop pushing on mouse release
            pushing = False
            prev_mouse_pos = None

        elif event.type == pygame.MOUSEMOTION:
            # If in pushing mode, calculate mouse movement delta
            if pushing and prev_mouse_pos is not None:
                current_mouse_pos = Vector2(event.pos)
                mouse_delta = current_mouse_pos - prev_mouse_pos
                # Add a scaled version of mouse movement to the ball's velocity
                ball_vel += mouse_delta * 0.5  # Adjust the multiplier for sensitivity
                prev_mouse_pos = current_mouse_pos

    # Update ball position based on velocity
    ball_pos += ball_vel

    # Apply friction to gradually slow down the ball over time
    ball_vel *= friction

    # Bounce off the walls
    if ball_pos.x - ball_radius < 0:
        ball_pos.x = ball_radius
        ball_vel.x = -ball_vel.x
    if ball_pos.x + ball_radius > WIDTH:
        ball_pos.x = WIDTH - ball_radius
        ball_vel.x = -ball_vel.x
    if ball_pos.y - ball_radius < 0:
        ball_pos.y = ball_radius
        ball_vel.y = -ball_vel.y
    if ball_pos.y + ball_radius > HEIGHT:
        ball_pos.y = HEIGHT - ball_radius
        ball_vel.y = -ball_vel.y

    # Rendering
    screen.fill((30, 30, 30))  # Dark background
    pygame.draw.circle(
        screen, (255, 0, 0), (int(ball_pos.x), int(ball_pos.y)), ball_radius
    )
    pygame.display.flip()

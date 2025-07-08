import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Player constants
PLAYER_SIZE = 15  # Adjusted size
PLAYER_SPEED = 5
JUMP_HEIGHT = 10  

# Obstacle constants
OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 50
GAP_SIZE = 200

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Geometry Dash-like Game")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Player
player_x = WIDTH // 4
player_y = HEIGHT // 2
player_velocity = 0

# Obstacles
obstacles = []

# Function to generate random obstacles
def generate_obstacle():
    obstacle_height = random.randint(100, HEIGHT - GAP_SIZE - 100)
    obstacle_top = pygame.Rect(WIDTH, 0, OBSTACLE_WIDTH, obstacle_height)
    obstacle_bottom = pygame.Rect(WIDTH, obstacle_height + GAP_SIZE, OBSTACLE_WIDTH, HEIGHT - obstacle_height - GAP_SIZE)
    return obstacle_top, obstacle_bottom

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_velocity = -JUMP_HEIGHT

    # Player movement
    player_y += player_velocity
    player_velocity += 1  # Gravity

    # Generate obstacles
    if random.randint(0, 100) < 5:  # Adjust the probability based on your preference
        obstacles.extend(generate_obstacle())

    # Move obstacles
    obstacles = [obstacle.move(-PLAYER_SPEED, 0) for obstacle in obstacles]

    # Remove off-screen obstacles
    obstacles = [obstacle for obstacle in obstacles if obstacle.right > 0]

    # Check for collisions with obstacles
    player_rect = pygame.Rect(player_x, player_y, PLAYER_SIZE, PLAYER_SIZE)
    if any(player_rect.colliderect(obstacle) for obstacle in obstacles):
        print("Game Over!")
        pygame.quit()
        sys.exit()

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, (player_x, player_y, PLAYER_SIZE, PLAYER_SIZE))  # Player
    for obstacle in obstacles:
        pygame.draw.rect(screen, RED, obstacle)  # Obstacles

    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

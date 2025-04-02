import pygame
import random
import sys
import os

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 350, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game with Coins")

# Colors
WHITE = (247, 247, 247)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Load assets
# Make sure you have a car image
car = pygame.image.load(os.path.join("lab_8", "images", "car.png"))
car = pygame.transform.scale(car, (75, 150))

# Car settings
car_x = WIDTH // 2 - 25
car_y = HEIGHT - 120
car_speed = 5

# Coin settings
coin_size = 20
coins = []  # List to store coins
coin_spawn_time = 0
coin_spawn_delay = 700  # Spawn a coin every 1 second
collected_coins = 0

# Font settings
font = pygame.font.Font(None, 36)

# Game loop
clock = pygame.time.Clock()
run = True
while run:
    screen.fill(WHITE)  # Clear screen

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get pressed keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < WIDTH - 50:
        car_x += car_speed

    # Coin spawning logic
    if pygame.time.get_ticks() - coin_spawn_time > coin_spawn_delay:
        # Random position on the road
        coin_x = random.randint(15, WIDTH - 15)
        coin_y = -coin_size  # Start above the screen
        coins.append([coin_x, coin_y])
        coin_spawn_time = pygame.time.get_ticks()

    # Move and draw coins
    for coin in coins[:]:
        coin[1] += 4  # Move coin downwards
        pygame.draw.circle(screen, YELLOW, (coin[0], coin[1]), coin_size // 2)

        # Check for collision with car
        if (car_x < coin[0] < car_x + 50) and (car_y < coin[1] < car_y + 100):
            collected_coins += 1
            coins.remove(coin)  # Remove collected coin

        # Remove coins that move off the screen
        elif coin[1] > HEIGHT:
            coins.remove(coin)

    # Draw the car
    screen.blit(car, (car_x, car_y))

    # Display collected coins count
    coin_text = font.render(f"Coins: {collected_coins}", True, BLACK)
    screen.blit(coin_text, (WIDTH - 150, 10))

    # Update display
    pygame.display.flip()
    clock.tick(60)

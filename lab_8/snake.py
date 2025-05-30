import pygame
import sys
pygame.init()


screen = pygame.display.set_mode((500, 500))
cell_size = 10
pygame.display.set_caption("Snake game")
bg_clr = pygame.Color("white")
snake_color = pygame.Color("red")

snake_pos = [100, 100]
snake_body = [[100, 100], [80, 100], [60, 100]]
direction = "RIGHT"
change_to = direction

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                change_to = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                change_to = "DOWN"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                change_to = "RIGHT"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                change_to = "LEFT"
    direction = change_to

    if direction == "UP":
        snake_pos[1] -= cell_size
    elif direction == "DOWN":
        snake_pos[1] += cell_size
    elif direction == "LEFT":
        snake_pos[0] -= cell_size
    elif direction == "RIGHT":
        snake_pos[0] += cell_size

    if snake_pos[0] < 0:
        snake_pos[0] = 500
    elif snake_pos[0] > 500:
        snake_pos[0] = 0
    elif snake_pos[1] < 0:
        snake_pos[1] = 500
    elif snake_pos[1] > 500:
        snake_pos[1] = 0

    snake_body.insert(0, list(snake_pos))
    snake_body.pop()

    screen.fill(bg_clr)
    for block in snake_body:
        pygame.draw.rect(screen, snake_color, pygame.Rect(
            block[0], block[1], cell_size, cell_size))
    pygame.display.flip()
    clock.tick(6)

pygame.quit()
sys.exit()

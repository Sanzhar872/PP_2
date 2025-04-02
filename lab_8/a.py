import pygame

pygame.init()
screen = pygame.display.set_mode((400, 400))
white = (255, 255, 255)


class Button:
    def __init__(self, x, y, width, height, text, color, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.action = action

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.Font(None, 24)
        text_surface = font.render(self.text, True, white)
        screen.blit(text_surface, (self.rect.x + 12, self.rect.y + 12))

    def check_action(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.action()
# Функция, вызываемая при нажатии на кнопку


def start_game():
    print("Игра началась!")


# Создаем кнопку
btn = Button(100, 200, 150, 50, "Start", (0, 255, 0), start_game)

running = True
while running:
    screen.fill(white)  # Очищаем экран
    btn.draw(screen)  # Рисуем кнопку

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        btn.check_action(event)  # Проверяем, нажали ли кнопку

    pygame.display.flip()

pygame.quit()

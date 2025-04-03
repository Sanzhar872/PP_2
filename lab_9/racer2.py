import pygame
import sys
from pygame.locals import *
import random
import time
import os

# Initializing
pygame.init()

# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GOLD = (255, 215, 0)

# Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS_COLLECTED = 0
COIN_THRESHOLD = 5  # Number of coins needed to increase speed
COIN_FALL_SPEED = 3  # Slower falling speed for coins

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load(os.path.join(
    "lab_8", "images", "AnimatedStreet.png"))

# Create a white screen
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(
            os.path.join("lab_8", "images", "Enemy.png"))
        # оздаёт прямоугольник который оборачивает картинку врага
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(
            40, SCREEN_WIDTH-40), 0)  # координаты Врага

    def move(self):
        global SCORE
        # это метод Pygame, который перемещает объект (по Х не двигается а по Y speed)
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:  # это Y-координата если он больше 600 значит враг уже скрылся
            SCORE += 1  # добавляем очко
            self.rect.top = 0  # сбрасываем врага
            # новыве координаты врага
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(
            os.path.join("lab_8", "images", "Player.png"))
        self.rect = self.image.get_rect()  # обарачиваем нашу машину в рект
        self.rect.center = (160, 520)  # ее координаты

    def move(self):
        pressed_keys = pygame.key.get_pressed()  # получаем какие кнопки были нажаты
        if self.rect.left > 0:  # проверяем что он не уехал за левую границу
            if pressed_keys[K_LEFT]:
                # сдвигаем игрока на 5 пикселей на лева
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:  # проверяем что он не уехал за правую границу
            if pressed_keys[K_RIGHT]:
                # сдвигаем игрока на 5 пикселей на лева
                self.rect.move_ip(5, 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.radius = random.randint(5, 10)  # разные радиусы монет
        self.image = pygame.Surface(
            (self.radius * 2, self.radius * 2), pygame.SRCALPHA)  # создаем поверхность ширина = радиус * 2, высота = радиус * 2
        pygame.draw.circle(
            self.image, GOLD, (self.radius, self.radius), self.radius)  # рисуем монеты золотого цвета внутри нашей поверхности
        self.rect = self.image.get_rect()  # оборачиваем монету в рект
        # даем рандомную координату
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        # монета падает вниз с фиксированной скоросью
        self.rect.move_ip(0, COIN_FALL_SPEED)
        if self.rect.top > 600:  # если Y > 600 то монета уже скрылась
            self.rect.top = 0  # создаем новую монету
            # новые координаты монеты
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


# Содаем объекты
P1 = Player()
E1 = Enemy()
coins = pygame.sprite.Group()

# Создаем пару монет
for _ in range(3):
    coins.add(Coin())

# Содаем группу спрайтов
# Содаем группу спрайтов enemises можно проверять на сталкивание с игроком
enemies = pygame.sprite.Group()
enemies.add(E1)  # добавляем в группу E1(врага)
all_sprites = pygame.sprite.Group()  # Создаем общую группу срайтов
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(*coins)  # добавляем все объекты из Coins по отдельности

# Adding a new User event
INC_SPEED = pygame.USEREVENT + 1  # пользовательские события.
# Настраиваем таймер, чтобы событие срабатывало каждые 1000 мс
pygame.time.set_timer(INC_SPEED, 1000)

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:  # проверяем сработало ли на наше событие которые обнавляеться каждую секнуду
            SPEED += 0.5  # если да то увеличиваем скорость нашего enemy
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # рисуем нашу улицу на экране через координаты 0,0
    DISPLAYSURF.blit(background, (0, 0))
    # очки шрифта и размера font_small и преобразованные очки в стринг
    scores = font_small.render(str(SCORE), True, BLACK)
    coins_text = font_small.render(
        "Coins: " + str(COINS_COLLECTED), True, BLACK)  # количества монет шрифта и размера font_small
    DISPLAYSURF.blit(scores, (10, 10))  # выводим очки на позицию 10, 10
    # выводим монеты на координа width - 100, 10
    DISPLAYSURF.blit(coins_text, (SCREEN_WIDTH - 100, 10))

    for entity in all_sprites:  # перебираем все спрайты
        # эта строка рисует изображение текущего объекта на экране в том месте, где находится его прямоугольник
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()  # двигаем объект

    # функуия проверяет есть ли столкновение между двумя спрайтами (P1 и enemies)
    if pygame.sprite.spritecollideany(P1, enemies):
        time.sleep(0.5)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()  # если есть то экран станет красным выйдет надпись гейм овер и проведеться опреация sys.exit()

    # проверяем на столкновения между двумя спрайтами (P1, coins) есди да то удаляем монету
    for coin in pygame.sprite.spritecollide(P1, coins, True):
        COINS_COLLECTED += 1
        new_coin = Coin()
        coins.add(new_coin)
        all_sprites.add(new_coin)

        if COINS_COLLECTED % COIN_THRESHOLD == 0:
            SPEED += 1

    pygame.display.update()
    FramePerSec.tick(FPS)

import pygame, sys, random, time
from pygame.locals import *

pygame.init()

FPS = 120
FramePerSec = pygame.time.Clock()

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 2
SCORE = 0  
COINS = 0  

font = pygame.font.SysFont("Verdana", 60)  
font_small = pygame.font.SysFont("Verdana", 20)  
game_over = font.render("Game Over", True, BLACK)  

background = pygame.image.load(r"C:\Users\Yeldos\Downloads\street.png")

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Race")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"C:\Users\Yeldos\Downloads\enemy.png")  
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0) 

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED) # Двигаем вниз
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1  # Увеличиваем очки
            self.rect.top = 0  # Перемещаем врага наверх
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"C:\Users\Yeldos\Downloads\coin.png")  
        self.image = pygame.transform.scale(self.image, (30, 30))  # Уменьшаем размер
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  # Начальное положение

    def move(self):
        self.rect.move_ip(0, SPEED)  # Двигаем вниз
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0  # Перемещаем монету наверх
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Класс игрока (управляемая машина)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"C:\Users\Yeldos\Downloads\player.png")  
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)  # Начальная позиция игрока

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)  # Движение влево
        if pressed_keys[K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.move_ip(5, 0)  # Движение вправо

# Создание игровых объектов
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Группы спрайтов
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# Создание пользовательского события для увеличения скорости
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Игровой цикл
while True:
    # Обрабатываем события
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.3  # Увеличиваем скорость каждые 1 секунду
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Отрисовка фона и счёта
    DISPLAYSURF.blit(background, (0, 0))
    
    score_text = font_small.render(f"Score: {SCORE}", True, BLACK)
    coin_text = font_small.render(f"Coins: {COINS}", True, BLACK)
    
    DISPLAYSURF.blit(score_text, (10, 10))  # Очки врагов слева
    DISPLAYSURF.blit(coin_text, (300, 10))  # Количество монет справа

    # Обновляем положение всех объектов
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # Проверка столкновения игрока с врагом
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()  # Проигрываем звук аварии
        time.sleep(0.5)

        DISPLAYSURF.fill(RED)  # Красный экран при Game Over
        DISPLAYSURF.blit(game_over, (30, 250))  # Отображаем "Game Over"

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()  # Удаляем все спрайты
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Проверка столкновения игрока с монетой
    collected_coin = pygame.sprite.spritecollideany(P1, coins)
    if collected_coin:
        collected_coin.kill()  # Удаляем монету
        COINS += 1  # Увеличиваем счётчик монет

    # Если все монеты собраны, создаём новую монету
    if len(coins) == 0:
        new_coin = Coin()
        coins.add(new_coin)
        all_sprites.add(new_coin)

    # Обновляем экран и FPS
    pygame.display.update()
    FramePerSec.tick(FPS)
import pygame

# Инициализация Pygame
pygame.init()

# Установим размеры окна и создадим экран
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
pygame.display.set_caption("Anu")

# Начальные координаты и радиус круга
x, y = 400, 300  # Центр круга
radius = 30  # Радиус круга

# Основной цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обработка нажатий клавиш для сдвига круга
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        x -= 1  # Сдвиг влево
    if keys[pygame.K_d]:
        x += 1  # Сдвиг вправо
    if keys[pygame.K_w]:
        y -= 1  # Сдвиг вверх
    if keys[pygame.K_s]:
        y += 1  # Сдвиг вниз

    # Очистка экрана
    screen.fill((0, 0, 0))  # Черный фон

    # Отрисовка круга
    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)

    # Обновление экрана
    pygame.display.flip()

    # Ограничиваем FPS
    clock.tick(60)

# Завершение работы Pygame
pygame.quit()

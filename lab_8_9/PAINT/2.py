import pygame
import random

# Определение цветов
white = (255, 255, 255)
eraser = (0, 0, 0)  # Цвет для "ластика" (черный)
green = (34, 139, 34)
blue = (0, 0, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)

pygame.display.set_caption("Paint")  # Заголовок окна

# Основная функция приложения
def main():
    pygame.init()  # Инициализируем Pygame
    screen = pygame.display.set_mode((640, 480))  # Создаем окно приложения
    clock = pygame.time.Clock()  # Таймер для контроля FPS

    radius = 15  # Радиус кисти для рисования
    mode = white  # Текущий выбранный цвет
    last_pos = None  # Последняя позиция курсора для рисования линий

    # Главный игровой цикл
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                return  # Завершаем приложение при закрытии окна или нажатии Esc

            # Обработка смены цвета при нажатии клавиш
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    mode = red
                elif event.key == pygame.K_g:
                    mode = green
                elif event.key == pygame.K_b:
                    mode = blue
                elif event.key == pygame.K_y:
                    mode = yellow
                elif event.key == pygame.K_BACKSPACE:
                    mode = eraser
                elif event.key == pygame.K_x:
                    # Генерируем случайный цвет при нажатии 'x'
                    mode = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

                # При нажатии клавиш рисуются фигуры с текущим цветом
                elif event.key == pygame.K_w:
                    drawRectangle(screen, pygame.mouse.get_pos(), 200, 100, mode)
                elif event.key == pygame.K_c:
                    drawCircle(screen, pygame.mouse.get_pos(), mode)
                elif event.key == pygame.K_q:
                    drawSquare(screen, pygame.mouse.get_pos(), 100, mode)  # Рисуем квадрат
                elif event.key == pygame.K_t:
                    drawRightTriangle(screen, pygame.mouse.get_pos(), 100, mode)  # Рисуем прямоугольный треугольник
                elif event.key == pygame.K_e:
                    drawEquilateralTriangle(screen, pygame.mouse.get_pos(), 100, mode)  # Рисуем равносторонний треугольник
                elif event.key == pygame.K_d:
                    drawDiamond(screen, pygame.mouse.get_pos(), 100, mode)  # Рисуем ромб

            # При нажатии и перемещении мыши рисуется линия между последней позицией и текущей позицией курсора. 
            # Ширина линии и цвет зависят от выбранного режима.
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                last_pos = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEMOTION and event.buttons[0] and last_pos:
                drawLineBetween(screen, last_pos, pygame.mouse.get_pos(), radius, mode)
                last_pos = pygame.mouse.get_pos()

        pygame.display.flip()
        clock.tick(60)


# drawLineBetween() рисует линию между двумя точками, рассчитывая промежуточные точки и рисуя маленькие круги между ними для создания непрерывной линии.
def drawLineBetween(screen, start, end, width, color_mode):
    color = color_mode

    dx = start[0] - end[0]  # Рассчитываем горизонтальное расстояние
    dy = start[1] - end[1]  # Рассчитываем вертикальное расстояние

    iterations = max(abs(dx), abs(dy))  # Определяем количество шагов для плавности линии

    # Рисуем плавную линию
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)


# drawRectangle() рисует прямоугольник с центром в текущем положении курсора. Ширина и высота прямоугольника фиксированы.
def drawRectangle(screen, mouse_pos, w, h, color):
    x = mouse_pos[0]
    y = mouse_pos[1]
    rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, color, rect, 3)


# drawCircle() рисует круг с центром в текущем положении курсора. Радиус круга фиксирован.
def drawCircle(screen, mouse_pos, color):
    x = mouse_pos[0]
    y = mouse_pos[1]
    pygame.draw.circle(screen, color, (x, y), 100, 3)


# drawSquare() рисует квадрат с центром в текущем положении курсора.
def drawSquare(screen, mouse_pos, size, color):
    x = mouse_pos[0] - size // 2
    y = mouse_pos[1] - size // 2
    pygame.draw.rect(screen, color, pygame.Rect(x, y, size, size), 3)


# drawRightTriangle() рисует прямоугольный треугольник с заданным основанием и высотой.
def drawRightTriangle(screen, mouse_pos, size, color):
    x, y = mouse_pos
    points = [(x, y), (x + size, y), (x, y - size)]
    pygame.draw.polygon(screen, color, points, 3)


# drawEquilateralTriangle() рисует равносторонний треугольник с заданной стороной.
def drawEquilateralTriangle(screen, mouse_pos, size, color):
    x, y = mouse_pos
    height = (3 ** 0.5 / 2) * size  # Высота равностороннего треугольника
    points = [
        (x, y - height / 2),
        (x - size / 2, y + height / 2),
        (x + size / 2, y + height / 2)
    ]
    pygame.draw.polygon(screen, color, points, 3)


# drawDiamond() рисует ромб с центром в текущем положении курсора.
def drawDiamond(screen, mouse_pos, size, color):
    x, y = mouse_pos
    points = [
        (x, y - size),  # Верхняя вершина
        (x + size, y),  # Правая вершина
        (x, y + size),  # Нижняя вершина
        (x - size, y)   # Левая вершина
    ]
    pygame.draw.polygon(screen, color, points, 3)


# Запуск основного цикла
main()

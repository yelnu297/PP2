import pygame
import time
import random
import psycopg2
 
# Подключение к базе данных
conn = psycopg2.connect(
    host="localhost",
    database="snake_anu",
    user="postgres",
    password="123456"
)
cur = conn.cursor()
 
# Создание таблиц
def create_tables():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS "user" (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            level INTEGER DEFAULT 1
        );
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS user_score (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES "user"(id),
            score INTEGER DEFAULT 0,
            saved_state TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    conn.commit()
 
create_tables()
 
# Получение или создание пользователя
def get_user_id(username):
    cur.execute("SELECT id, level FROM \"user\" WHERE username = %s", (username,))
    result = cur.fetchone()
    if result:
        return result[0], result[1]
    else:
        cur.execute("INSERT INTO \"user\" (username) VALUES (%s) RETURNING id", (username,))
        conn.commit()
        return cur.fetchone()[0], 1
 
# Обновление уровня пользователя
def update_user_level(user_id, new_level):
    cur.execute("UPDATE \"user\" SET level = %s WHERE id = %s", (new_level, user_id))
    conn.commit()
 
# Сохранение очков
def save_score(user_id, score, state=None):
    cur.execute(
        "INSERT INTO user_score (user_id, score, saved_state) VALUES (%s, %s, %s)",
        (user_id, score, str(state))
    )
    conn.commit()
 
# Удаление пользователя
def delete_user(username):
    try:
        cur.execute('SELECT id FROM "user" WHERE username = %s', (username,))
        user = cur.fetchone()
 
        if user is None:
            print(f"user '{username}' not found.")
            return
 
        user_id = user[0]
        cur.execute("DELETE FROM user_score WHERE user_id = %s", (user_id,))
        cur.execute('DELETE FROM "user" WHERE id = %s', (user_id,))
        conn.commit()
        print(f"user '{username}' has deleted ")
    except Exception as e:
        print(f"error: {e}")
        conn.rollback()
 
# Инициализация Pygame
pygame.init()
window_x = 720
window_y = 480
game_window = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption('Snake Game')
fps = pygame.time.Clock()
 
# Цвета
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
 
# Настройки игры
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
food_types = [(10, white), (20, blue), (30, red)]
snake_speed = 10
score = 0
direction = 'RIGHT'
change_to = direction
 
# Спавн еды
def spawn_food():
    weight, color = random.choice(food_types)
    return [random.randrange(1, (window_x // 10)) * 10,
            random.randrange(1, (window_y // 10)) * 10,
            weight, color, time.time()]
 
food = spawn_food()
 
# Отображение счёта
def show_score(color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render(f'Score : {score}', True, color)
    game_window.blit(score_surface, (10, 10))
 
# Завершение игры
def game_over():
    save_score(user_id, score)
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render(f'Your Score is : {score}', True, red)
    game_window.blit(game_over_surface, (window_x // 4, window_y // 4))
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()
 
# Ввод имени игрока
def get_player_name():
    font = pygame.font.SysFont('times new roman', 30)
    input_box = pygame.Rect(window_x // 3, window_y // 3, 200, 50)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    clock = pygame.time.Clock()
 
    while True:
        game_window.fill(black)
        txt_surface = font.render(text, True, color)
        game_window.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(game_window, color, input_box, 2)
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = True
                    color = color_active
                else:
                    active = False
                    color = color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return text
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
 
        pygame.display.flip()
        clock.tick(30)
 
# Кнопка удаления пользователя
def delete_user_button(username):
    font = pygame.font.SysFont('times new roman', 30)
    button_rect = pygame.Rect(window_x // 3, window_y // 2 + 100, 200, 50)
 
    while True:
        game_window.fill(black)
        title_text = font.render(f' {username}', True, white)
        game_window.blit(title_text, (window_x // 3, window_y // 3 - 60))
 
        pygame.draw.rect(game_window, red, button_rect)
        delete_text = font.render("Delete User", True, black)
        game_window.blit(delete_text, (button_rect.x + 30, button_rect.y + 10))
 
        info_text = font.render("Enter to cont", True, white)
        game_window.blit(info_text, (window_x // 3 - 40, window_y // 2))
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    delete_user(username)
                    pygame.quit()
                    quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return
 
        pygame.display.flip()
 
# Выбор уровня
def level_selection():
    font = pygame.font.SysFont('times new roman', 30)
    button_width, button_height = 200, 50
    button_x = window_x // 3
    button_y = window_y // 3
 
    easy_button = pygame.Rect(button_x, button_y, button_width, button_height)
    medium_button = pygame.Rect(button_x, button_y + 60, button_width, button_height)
    hard_button = pygame.Rect(button_x, button_y + 120, button_width, button_height)
 
    while True:
        game_window.fill(black)
        pygame.draw.rect(game_window, green, easy_button)
        pygame.draw.rect(game_window, blue, medium_button)
        pygame.draw.rect(game_window, red, hard_button)
 
        easy_text = font.render("Level 1", True, black)
        medium_text = font.render("Level 2", True, black)
        hard_text = font.render("Level 3", True, black)
 
        game_window.blit(easy_text, (button_x + 50, button_y + 10))
        game_window.blit(medium_text, (button_x + 50, button_y + 70))
        game_window.blit(hard_text, (button_x + 50, button_y + 130))
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_button.collidepoint(event.pos):
                    return 1
                elif medium_button.collidepoint(event.pos):
                    return 2
                elif hard_button.collidepoint(event.pos):
                    return 3
 
        pygame.display.flip()
 
# --- Запуск игры ---
 
player_name = get_player_name()
user_id, current_level = get_user_id(player_name)
 
# Показываем кнопку удаления
delete_user_button(player_name)
 
# Уровень
selected_level = level_selection()
update_user_level(user_id, selected_level)
 
# Скорость змеи
snake_speed = 10 + (selected_level - 1) * 5
 
# Главный цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_score(user_id, score)
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'
            elif event.key == pygame.K_p:
                state = {
                    'snake_position': snake_position,
                    'snake_body': snake_body,
                    'direction': direction,
                    'score': score
                }
                save_score(user_id, score, state)
                print("⏸ Игра сохранена!")
 
    direction = change_to
 
    if direction == 'UP':
        snake_position[1] -= 10
    elif direction == 'DOWN':
        snake_position[1] += 10
    elif direction == 'LEFT':
        snake_position[0] -= 10
    elif direction == 'RIGHT':
        snake_position[0] += 10
 
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == food[0] and snake_position[1] == food[1]:
        score += food[2]
        food = spawn_food()
    else:
        snake_body.pop()
 
    if time.time() - food[4] > 5:
        food = spawn_food()
 
    game_window.fill(black)
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, food[3], pygame.Rect(food[0], food[1], 10, 10))
 
    if (snake_position[0] < 0 or snake_position[0] > window_x - 10 or
        snake_position[1] < 0 or snake_position[1] > window_y - 10):
        game_over()
 
    for block in snake_body[1:]:
        if snake_position == block:
            game_over()
 
    show_score(white, 'times new roman', 20)
    pygame.display.update()
    fps.tick(snake_speed)
 
import pygame
import random
import time
import psycopg2
from datetime import datetime

conn = psycopg2.connect(
    dbname="snake_db",
    user="postgres",
    password="123456", 
    host="localhost",
    port="5432"
)
cur = conn.cursor()

def get_or_create_user(username):
    cur.execute("SELECT level FROM users WHERE username = %s", (username,))
    result = cur.fetchone()
    if result:
        return username, result[0]
    else:
        cur.execute("INSERT INTO users (username, level) VALUES (%s, %s)", (username, 1))
        conn.commit()
        return username, 1

def save_progress(username, score, level):
    cur.execute("INSERT INTO user_scores (user_id, score, level) VALUES (%s, %s, %s)", (username, score, level))
    cur.execute("UPDATE users SET level = %s WHERE username = %s", (level, username))
    conn.commit()

pygame.init()
screen_width, screen_height = 600, 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game with DB")
font = pygame.font.SysFont("Arial", 24)

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

snake_size = 20
grid_size = 20
clock = pygame.time.Clock()

class Food:
    def __init__(self, x, y, weight):
        self.x = x
        self.y = y
        self.weight = weight
        self.timestamp = time.time()

    def is_expired(self, duration):
        return time.time() - self.timestamp > duration

def generate_food():
    x = random.randrange(0, screen_width, grid_size)
    y = random.randrange(0, screen_height, grid_size)
    weight = random.choice([1, 2, 3])
    return Food(x, y, weight)

def username_input_screen():
    input_box = pygame.Rect(150, 180, 300, 40)
    user_text = ""
    active = True

    while active:
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, input_box, 2)

        text_surface = font.render("Enter your username:", True, WHITE)
        screen.blit(text_surface, (150, 140))
        user_surface = font.render(user_text, True, WHITE)
        screen.blit(user_surface, (input_box.x + 5, input_box.y + 5))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and user_text.strip():
                    return user_text.strip()
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode

def game_loop(username, start_level):
    snake = [(100, 100), (80, 100), (60, 100)]
    direction = 'RIGHT'
    score = 0
    level = start_level
    speed = 10 + (level - 1) * 2

    food_list = [generate_food()]
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != 'RIGHT':
                    direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    direction = 'RIGHT'
                elif event.key == pygame.K_UP and direction != 'DOWN':
                    direction = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    direction = 'DOWN'
                elif event.key == pygame.K_p:
                    save_progress(username, score, level)
                    paused = True
                    while paused:
                        for e in pygame.event.get():
                            if e.type == pygame.KEYDOWN and e.key == pygame.K_p:
                                paused = False

        x, y = snake[0]
        if direction == 'LEFT': x -= grid_size
        elif direction == 'RIGHT': x += grid_size
        elif direction == 'UP': y -= grid_size
        elif direction == 'DOWN': y += grid_size

        if x < 0 or x >= screen_width or y < 0 or y >= screen_height:
            break

        snake = [(x, y)] + snake[:-1]

        if (x, y) in snake[1:]:
            break   

        for food in food_list[:]:
            if x == food.x and y == food.y:
                food_list.remove(food)
                snake.append(snake[-1])
                score += food.weight
                if score >= level * 3:
                    level += 1
                    speed += 2

        food_list = [f for f in food_list if not f.is_expired(5)]
        if random.random() < 0.05:
            food_list.append(generate_food())

        screen.fill(BLACK)
        for part in snake:
            pygame.draw.rect(screen, GREEN, (*part, snake_size, snake_size))
        for food in food_list:
            pygame.draw.rect(screen, RED, (food.x, food.y, snake_size, snake_size))

        screen.blit(font.render(f"Score: {score}", True, WHITE), (10, 10))
        screen.blit(font.render(f"Level: {level}", True, WHITE), (10, 40))

        pygame.display.update()
        clock.tick(speed)

    save_progress(username, score, level)
    pygame.quit()

if __name__ == "__main__":
    username = username_input_screen()
    user, level = get_or_create_user(username)
    game_loop(user, level)
    cur.close()
    conn.close()


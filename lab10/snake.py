import pygame
import time
import random
import psycopg2

conn = psycopg2.connect(
    dbname='phoneboook',
    user='alyeavui',
    password='1234',
    host='localhost',
    port='5432'
)

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users
              (id SERIAL PRIMARY KEY, username TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS user_scores
              (id SERIAL PRIMARY KEY, user_id INTEGER, score INTEGER, level INTEGER)''')
conn.commit()

pygame.init()

WIDTH = 600
HEIGHT = 600
CELL = 30
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

colorWHITE = (255, 255, 255)
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)
colorYELLOW = (255, 255, 0)
colorBLUE = (0, 0, 255)
colorGRAY = (128, 128, 128)
colorBLACK = (0, 0, 0)

level_speeds = [5, 7, 9] 
level_walls = [[(10, 10), (10, 11), (10, 12)], [(15, 15), (15, 16), (15, 17)], [(5, 5), (5, 6), (5, 7)]]  # Walls for each level
level = 1
score = 0
snake_speed = level_speeds[level - 1]
super_food_active = False

font = pygame.font.SysFont("Verdana", 30)

username = input("Enter your username: ")

cursor.execute('SELECT id FROM users WHERE username = %s', (username,))
user_row = cursor.fetchone()
if user_row is None:
    cursor.execute('INSERT INTO users (username) VALUES (%s) RETURNING id', (username,))
    user_id = cursor.fetchone()[0]
else:
    user_id = user_row[0]
    cursor.execute('SELECT level FROM user_scores WHERE user_id = %s ORDER BY id DESC LIMIT 1', (user_id,))
    row = cursor.fetchone()
    if row is not None:
        level = row[0]
    snake_speed = level_speeds[level - 1]

def update_user_score(user_id, score, level):
    cursor.execute('INSERT INTO user_scores (user_id, score, level) VALUES (%s, %s, %s)', (user_id, score, level))
    conn.commit()

def draw_grid():
    for x in range(0, WIDTH, CELL):
        pygame.draw.line(screen, colorGRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL):
        pygame.draw.line(screen, colorGRAY, (0, y), (WIDTH, y))

def draw_walls(level):
    for wall_segment in level_walls[level - 1]:
        pygame.draw.rect(screen, colorBLUE, (wall_segment[0] * CELL, wall_segment[1] * CELL, CELL, CELL))

def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, colorGREEN, (segment[0] * CELL, segment[1] * CELL, CELL, CELL))

def draw_food(food):
    pygame.draw.rect(screen, colorRED, (food[0] * CELL, food[1] * CELL, CELL, CELL))

def generate_food_position(snake, level):
    while True:
        food = (random.randint(0, (WIDTH // CELL) - 1), random.randint(0, (HEIGHT // CELL) - 1))
        if food not in snake and food not in level_walls[level - 1]:
            return food

snake = [(5, 5)]
dx, dy = 1, 0
food = generate_food_position(snake, level)

clock = pygame.time.Clock()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dy != 1:
                dx, dy = 0, -1
            elif event.key == pygame.K_DOWN and dy != -1:
                dx, dy = 0, 1
            elif event.key == pygame.K_LEFT and dx != 1:
                dx, dy = -1, 0
            elif event.key == pygame.K_RIGHT and dx != -1:
                dx, dy = 1, 0
            elif event.key == pygame.K_p: 
                update_user_score(user_id, score, level)

    new_head = (snake[0][0] + dx, snake[0][1] + dy)
    if new_head in snake or new_head[0] < 0 or new_head[0] >= WIDTH // CELL or new_head[1] < 0 or new_head[1] >= HEIGHT // CELL:
        break
    snake.insert(0, new_head)

    if new_head == food:
        score += 1
        snake_speed += 0.1
        food = generate_food_position(snake, level)
    else:
        snake.pop()

    screen.fill(colorBLACK)
    draw_grid()
    draw_walls(level)
    draw_snake(snake)
    draw_food(food)
    text = font.render(f"Score: {score} Level: {level}", True, colorWHITE)
    screen.blit(text, (10, 10))
    pygame.display.flip()
    clock.tick(snake_speed)

    if score > level * 3 and level < len(level_speeds):
        level += 1
        snake_speed = level_speeds[level - 1]

game_over_text = font.render("Game Over", True, colorWHITE)
screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 30))
pygame.display.flip()
time.sleep(2)

update_user_score(user_id, score, level)

conn.close()
pygame.quit()

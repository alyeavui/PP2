import pygame
import random
import time
import psycopg2

pygame.init()

conn = psycopg2.connect(host="localhost", dbname="postgres", user="alyeavui", password="1234", port=5432)
cur = conn.cursor()

cur.execute('''DROP TABLE IF EXISTS users''')

cur.execute('''CREATE TABLE IF NOT EXISTS users(
            id INT PRIMARY KEY,
            name VARCHAR(255),
            score INT);
''')

Dict = {}

GREEN = (0,255,0)    
BLACK = (0,0,0)      
ORANGE = (255,165,0) 
PURPLE = (255,0,255) 
RED = (255,0,0)  
WHITE = (255,255,255)

WIDTH = 600
HEIGHT = 400

SCREEN = pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("Snake Game")      

clock = pygame.time.Clock()

snake_size = 10  

message_font = pygame.font.SysFont('ubuntu', 30)  
score_font = pygame.font.SysFont('ubuntu', 25)   
level_font = pygame.font.SysFont('ubuntu', 25)
USER_NAME = ''
ID = 0


def pause():
    paused = True
    while paused :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_c:
                    paused = False
                
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

def write_name():
    base_font = pygame.font.Font(None,35)
    user_name = ''
    input_rect = pygame.Rect(250,150, 140,32)
    color_active = pygame.Color('lightskyblue3')
    color_passive = pygame.Color('gray15')
    color = color_passive

    active = False

    while True:
        for event in pygame.event.get():
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run_game()
                if active == True:
                    if event.key == pygame.K_BACKSPACE:
                        user_name = user_name[:-1]
                    else:
                        user_name += event.unicode
        
        SCREEN.fill(BLACK)

        if active:
            color = color_active
        else:
            color = color_passive

        pygame.draw.rect(SCREEN, color, input_rect,2)

        text_surface = base_font.render(user_name, True, WHITE)
        SCREEN.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

        input_rect.w = max(100,text_surface.get_width() + 10)

        global USER_NAME
        USER_NAME = user_name

        pygame.display.flip()


def print_score(score):
    text = score_font.render("Score: " + str(score) , True , ORANGE)
    SCREEN.blit(text, (0,0))

def print_level(level_snake):
    level = level_font.render("Level: " + str(level_snake) , True , ORANGE)
    SCREEN.blit(level,(200,0))

def draw_snake(snake_size, snake_pixels) : 
    for pixels in snake_pixels :        
        pygame.draw.rect(SCREEN, GREEN, (pixels[0], pixels[1], snake_size , snake_size))

def run_game():
    game_over = False 
    game_close = False 

    x = WIDTH / 2  
    y = HEIGHT / 2

    x_speed = 0 
    y_speed = 0

    snake_pixels = [] 
    snake_length = 1  

    food_x = round(random.randrange(0, WIDTH - snake_size) / 10) * 10
    food_y = round(random.randrange(0, HEIGHT - snake_size) / 10) * 10

    food2_x = round(random.randrange(0, WIDTH - snake_size) / 10) * 10
    food2_y = round(random.randrange(0, HEIGHT - snake_size) / 10) * 10

    count = 0 
    level_snake = 0  

    snake_speed = 10 

    timer, timer2 = 50, 50  

    
    while not game_over :
        while game_close :
            
            game_over_message = message_font.render("Game Over!" , True, RED)
            user_name_message = message_font.render("Username: " + USER_NAME, True, WHITE)
            score_message = score_font.render("Score: " + str(snake_length-1), True, WHITE)
            SCREEN.blit(game_over_message , (WIDTH / 3, HEIGHT / 3))
            SCREEN.blit(user_name_message , (WIDTH / 3 , HEIGHT / 3 + 30))
            SCREEN.blit(score_message , (WIDTH / 3, HEIGHT / 3 + 60))
            print_score(snake_length - 1)
            user_score = snake_length - 1
            global ID

            cur.execute('''INSERT INTO users (id, name, score) VALUES
                        (%s, %s, %s)''',(ID,USER_NAME, user_score))
            ID+=1

            cur.execute('SELECT * FROM users')
            for i in cur.fetchall():
                print(i)

            conn.commit()
            cur.close()
            conn.close()

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    game_over = True    
                    game_close = False  
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1: 
                        game_over = True   
                        game_close = False
                    if event.key == pygame.K_2: 
                        write_name()
                        run_game()
                        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_LEFT:
                    x_speed = -snake_size  
                    y_speed = 0
                if event.key == pygame.K_RIGHT :
                    x_speed = snake_size
                    y_speed = 0
                if event.key == pygame.K_UP :
                    x_speed = 0
                    y_speed = -snake_size
                if event.key == pygame.K_DOWN :
                    x_speed = 0
                    y_speed = snake_size
                if event.key == pygame.K_p:
                    pause()
                timer -= 1   
                timer2 -= 1

        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0 :
            game_close = True
        
        x += x_speed 
        y += y_speed

        SCREEN.fill(BLACK)  
        
        pygame.draw.rect(SCREEN, ORANGE, (food_x, food_y, snake_size, snake_size)) 
        pygame.draw.rect(SCREEN, PURPLE, (food2_x, food2_y, snake_size, snake_size)) 
        snake_pixels.append((x,y)) 

        if len(snake_pixels) > snake_length :  
            del snake_pixels[0]

        for pixel in snake_pixels[:-1] :  
            if pixel == (x,y) :
                game_close = True 

        draw_snake(snake_size, snake_pixels)
        print_score(snake_length - 1)
        print_level(level_snake)

        if count >= 3 : 
            level_snake += 1
            snake_speed += 2  
            count = 0   

        pygame.display.update()

        if x == food_x and y == food_y : 
            food_x = round(random.randrange(0,WIDTH - snake_size) / 10) * 10   
            food_y = round(random.randrange(0,HEIGHT - snake_size) / 10) * 10
            snake_length += 1 
            count += 1 
            timer = 50  

        if timer <= 0:  
            food_x = round(random.randrange(0,WIDTH - snake_size) / 10) * 10   
            food_y = round(random.randrange(0,HEIGHT - snake_size) / 10) * 10
            timer =  50 

        if x == food2_x and y == food2_y : 
            food2_x = round(random.randrange(0,WIDTH - snake_size) / 10) * 10   
            food2_y = round(random.randrange(0,HEIGHT - snake_size) / 10) * 10
            snake_length += 2  
            count += 2 
            timer2 = 50 

        if timer2 <= 0 :  
            food2_x = round(random.randrange(0,WIDTH - snake_size) / 10) * 10   
            food2_y = round(random.randrange(0,HEIGHT - snake_size) / 10) * 10
            timer2 = 50  
        
        clock.tick(snake_speed) 
 
    pygame.quit()

write_name()

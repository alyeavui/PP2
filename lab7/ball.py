import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Move the Ball')

WHITE = (255, 255, 255)
RED = (255, 0, 0)

ball_radius = 25
ball_x, ball_y = 400, 300
ball_dx, ball_dy = 0, 0

def draw_ball(x, y):
    pygame.draw.circle(screen, RED, (x, y), ball_radius)

clock = pygame.time.Clock()

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball_dy = -20
            elif event.key == pygame.K_DOWN:
                ball_dy = 20
            elif event.key == pygame.K_LEFT:
                ball_dx = -20
            elif event.key == pygame.K_RIGHT:
                ball_dx = 20
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                ball_dy = 0
            elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                ball_dx = 0

    new_x = ball_x + ball_dx
    new_y = ball_y + ball_dy

    if ball_radius <= new_x <= 800 - ball_radius * 2:
        ball_x = new_x
    if ball_radius <= new_y <= 600 - ball_radius * 2:
        ball_y = new_y

    draw_ball(ball_x, ball_y)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()

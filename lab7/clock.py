import pygame
import math
from sys import exit

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Mickey')
clock = pygame.time.Clock()

mickeyclock = pygame.image.load('mickeyclock.jpeg')
mickeyclock = pygame.transform.scale(mickeyclock, (500, 500))

mickeyhand_minute = pygame.image.load('mickeyhand_minute.png')  
mickeyhand_second = pygame.image.load('clock-tongue-side.png')
mickeyhand_minute = pygame.transform.scale(mickeyhand_minute, (60, 60))
mickeyhand_second = pygame.transform.scale(mickeyhand_second, (100, 100))
minute_angle = 0
second_angle = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(mickeyclock, (0, 0))  
    minute_angle += 0.1
    rotated_minute = pygame.transform.rotate(mickeyhand_minute, -minute_angle)
    minute_rect = rotated_minute.get_rect(center=(250, 250))  
    screen.blit(rotated_minute, minute_rect)

    second_angle += 6  
    rotated_second = pygame.transform.rotate(mickeyhand_second, -second_angle)
    second_rect = rotated_second.get_rect(center=(250, 250)) 
    screen.blit(rotated_second, second_rect)

    pygame.display.update()
    clock.tick(60)  

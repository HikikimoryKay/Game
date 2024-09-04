import pygame
import random

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Арбуз арбуз привет')

WHITE = (255, 255, 255)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0, 0, 0)

square_size = 50
square_x = screen_width // 2
square_y = screen_height - square_size

ball_radius = 15
ball_x = random.randint(0, screen_width)
ball_y = random.randint(0, screen_height //2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and square_x > 0:
        square_x = square_x - 0.3
    if keys[pygame.K_RIGHT] and square_x < screen_width - square_size:
        square_x = square_x + 0.3
    if keys[pygame.K_UP] and square_y > 0:
        square_y = square_y - 0.3
    if keys[pygame.K_DOWN] and square_y < screen_height - square_size:
        square_y = square_y + 0.3

    ball_y = ball_y + 0.2
    if ball_y > screen_height:
        ball_y = 0
        ball_x = random.randint(0, screen_width)
    
    

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, (square_x, square_y, square_size, square_size))
    pygame.draw.circle(screen, GREEN, (ball_x, ball_y), ball_radius)
    pygame.display.update()

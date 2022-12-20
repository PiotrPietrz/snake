import pygame
import time

pygame.init()

# constants for the window size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
color = (0, 245, 0)
# the size of snake head
snake_1 = 20
snake_2 = 20
x = SCREEN_WIDTH / 2
y = SCREEN_HEIGHT / 2

surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
rect = pygame.Rect(x, y, snake_1, snake_2)

# how fast the snake moves
speed = 0.4

# variables for steering snake's movement
move_x = 0
move_y = 10

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # it accepts only when the right button is pressed -> use arrows to steer the snake movement
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move_x = 0
                move_y = -10
            elif event.key == pygame.K_DOWN:
                move_x = 0
                move_y = 10
            elif event.key == pygame.K_RIGHT:
                move_x = 10
                move_y = 0
            elif event.key == pygame.K_LEFT:
                move_x = -10
                move_y = 0

    surface.fill((255, 255, 255))
    pygame.draw.rect(surface, color, rect)
    rect = pygame.Rect.move(rect, move_x, move_y)
    pygame.display.update()

    time.sleep(speed)


pygame.quit()

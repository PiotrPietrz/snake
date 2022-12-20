import pygame
import time

pygame.init()

# constants for the window size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

color = (0, 245, 0)

# the size of snake head
snake_width = 20
snake_height = 20

# snake's starting point
x = SCREEN_WIDTH / 2
y = SCREEN_HEIGHT / 2

# creating a window and the snake
surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# how fast the snake moves
speed = 0.3

# variables for steering snake's movement
move_x = 0
move_y = 0

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # it accepts only when the right button is pressed -> use arrows to change the snake direction
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

    x += move_x
    y += move_y

    if x >= SCREEN_HEIGHT or x < 0 or y >= SCREEN_WIDTH or y < 0:
        run = False

    surface.fill((0, 0, 255))
    pygame.draw.rect(surface, color, [x, y, snake_width, snake_height])

    pygame.display.update()

    time.sleep(speed)


pygame.quit()
quit()

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


run = True

while run:
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.QUIT:
            run = False
    surface.fill((255, 255, 255))
    pygame.draw.rect(surface, color, rect)
    rect = pygame.Rect.move(rect, 0, 10)
    pygame.display.update()

    time.sleep(0.5)


pygame.quit()

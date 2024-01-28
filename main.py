import random

import pygame as pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

block_size = 40
snake_speed = 10


def draw_snake(block_size, snake_segments):
    for segment in snake_segments:
        pygame.draw.rect(screen, (0, 255, 0), [segment[0], segment[1], block_size, block_size])


def game_loop():
    game_over = False

    snake_x = screen.get_width() / 2
    snake_y = screen.get_height() / 2

    x_change = 0
    y_change = 0

    snake_list = []
    length_of_snake = 1

    # food position

    food_x = round(random.randrange(0, screen.get_width() - block_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, screen.get_height() - block_size) / 10.0) * 10.0

    while game_over == False:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -block_size
                    y_change = 0

                elif event.key == pygame.K_RIGHT:
                    x_change = block_size
                    y_change = 0

                elif event.key == pygame.K_UP:
                    y_change = -block_size
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = block_size
                    x_change = 0

        snake_x += x_change
        snake_y += y_change

        screen.fill('black')

        snake_head = []
        pygame.draw.rect(screen, 'red', [food_x, food_y, block_size, block_size])

        snake_head.append(snake_x)
        snake_head.append(snake_y)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]


        # Check for self-collision
        for x in snake_list[:-1]:
            if x == snake_head:
                game_over = True

        # check collison with boundaries

        if snake_x >= screen.get_width() or snake_x < 0 or snake_y >= screen.get_height() or snake_y < 0:
            game_over = True

        # draw snake

        draw_snake(block_size, snake_list)
        pygame.display.update()

        snake_head_rect = pygame.Rect(snake_x, snake_y, block_size, block_size)
        food_rect = pygame.Rect(food_x, food_y, block_size, block_size)

        # Check if snake eats food
        if snake_head_rect.colliderect(food_rect):
            food_x = round(random.randrange(0, screen.get_width() - block_size) / 10.0) * 10.0
            food_y = round(random.randrange(0, screen.get_height() - block_size) / 10.0) * 10.0
            length_of_snake += 1

        clock = pygame.time.Clock()
        clock.tick(snake_speed)
        pygame.display.flip()
    pygame.quit()
    quit()


game_loop()

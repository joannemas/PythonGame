import pygame
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)
pink = (255, 105, 180)
cyan = (0, 255, 255)

screen_width = 1000
screen_height = 600
tile_size = 25
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
snake_speed = 10

font_style = pygame.font.SysFont("Arial", 20)


def snake(tile_size, snake_body):
    for x in snake_body:
        pygame.draw.rect(screen, pink, [x[0], x[1], tile_size, tile_size])


def game():
    game_over = False
    game_close = False
    snake_coordinates = [screen_width / 2, screen_height / 2]
    snake_direction = [0, 0]
    snake_body = []
    snake_length = 1
    food = [round(random.randrange(0, screen_width - tile_size) / tile_size) * tile_size, round(random.randrange(0, screen_height - tile_size) / tile_size) * tile_size]

    while game_over == False:

        while game_close == True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_a:
                        game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_direction = [-tile_size, 0]
                elif event.key == pygame.K_RIGHT:
                    snake_direction = [tile_size, 0]
                elif event.key == pygame.K_UP:
                    snake_direction = [0, -tile_size]
                elif event.key == pygame.K_DOWN:
                    snake_direction = [0, tile_size]

        if snake_coordinates[0] >= screen_width or snake_coordinates[0] < 0 or snake_coordinates[1] >= screen_height or snake_coordinates[1] < 0:
            game_close = True
        snake_coordinates[0] += snake_direction[0]
        snake_coordinates[1] += snake_direction[1]

        screen.fill(black)
        pygame.draw.rect(screen, cyan, [food[0], food[1], tile_size, tile_size])
        snake_lead = [snake_coordinates[0], snake_coordinates[1]]
        snake_body.append(snake_lead)
        if len(snake_body) > snake_length:
            del snake_body[0]

        for x in snake_body[:-1]:
            if x == snake_lead:
                game_close = True

        snake(tile_size, snake_body)


        pygame.display.update()

        if snake_coordinates[0] == food[0] and snake_coordinates[1] == food[1]:
            food[0] = round(random.randrange(0, screen_width - tile_size) / tile_size) * tile_size
            food[1] = round(random.randrange(0, screen_height - tile_size) / tile_size) * tile_size
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


game()
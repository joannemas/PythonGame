import pygame
import random
from random import randrange

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
font_style = pygame.font.SysFont("arial", 25)


class Snake:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.body = []
        self.length = 1
        self.direction = [0, 0]

    def draw(self):
        for x in self.body:
            pygame.draw.rect(screen, pink, [x[0], x[1], self.size, self.size])

    def move(self):
        self.x += self.direction[0]
        self.y += self.direction[1]

        self.body.append([self.x, self.y])
        if len(self.body) > self.length:
            del self.body[0]

        for x in self.body[:-1]:
            if x == [self.x, self.y]:
                self.game_over()

        if self.x > screen_width - self.size or self.x < 0 or self.y > screen_height - self.size or self.y < 0:
            self.game_over()

    def game_over(self):
        print("Game Over")
        exit()

    def eat(self, food):
        if self.x == food.x and self.y == food.y:
            food.x = round(random.randrange(0, screen_width - self.size) / self.size) * self.size
            food.y = round(random.randrange(0, screen_height - self.size) / self.size) * self.size
            self.length += 1

class Food:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

    def draw(self):
        pygame.draw.rect(screen, cyan, [self.x, self.y, self.size, self.size])

class Score:
    def __init__(self, score):
        self.score = score

    def draw(self):
        value = font_style.render(f"Score : {str(self.score)}", True, yellow)
        screen.blit(value, [0, 0])

class Game:
    def __init__(self, width, height, size):
        self.width = width
        self.height = height
        self.size = size
        self.snake = Snake(self.width / 2, self.height / 2, self.size)
        self.food = Food(round(random.randrange(0, self.width - self.size) / self.size) * self.size, round(random.randrange(0, self.height - self.size) / self.size) * self.size, self.size)

    def draw(self):
        screen.fill(black)
        self.snake.draw()
        self.food.draw()
        self.score = Score(self.snake.length - 1)
        self.score.draw()

    def update(self):
        self.snake.move()
        self.snake.eat(self.food)

    def run(self):
        while True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.snake.direction = [-self.size, 0]
                    elif event.key == pygame.K_RIGHT:
                        self.snake.direction = [self.size, 0]
                    elif event.key == pygame.K_UP:
                        self.snake.direction = [0, -self.size]
                    elif event.key == pygame.K_DOWN:
                        self.snake.direction = [0, self.size]

            self.draw()
            self.update()
            pygame.display.update()
            clock.tick(snake_speed)

if __name__ == "__main__":
    game = Game(screen_width, screen_height, tile_size)
    game.run()
import pygame
import random
from game_elements import *

pygame.init()

class Game:
    def __init__(self, width, height, size):
        self.width = width
        self.height = height
        self.size = size
        self.snake = Snake(self.width / 2, self.height / 2, self.size)
        self.food = Food(round(random.randrange(0, self.width - self.size) / self.size) * self.size, round(random.randrange(0, self.height - self.size) / self.size) * self.size, self.size)
        self.obstacle = Obstacle(round(random.randrange(0, self.width - self.size) / self.size) * self.size, round(random.randrange(0, self.height - self.size) / self.size) * self.size, self.size)

    def draw(self):
        screen.fill(black)
        self.snake.draw()
        self.food.draw()
        self.score = Score(self.snake.length - 1)
        self.score.draw()
        if self.score.score > 4:
            self.obstacle.draw()

    def update(self):
        self.snake.move()
        self.snake.eat(self.food)
        self.snake.obstacle(self.obstacle)

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
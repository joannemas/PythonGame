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

        if Score(self.length - 1).score < 0:
            self.game_over()

    def game_over(self):
        screen.fill(pink)
        def message(msg, color):
                text = font_style.render(msg, True, color)
                screen.blit(text, [screen_width / 4, screen_height / 2])
        message("Perdu... Appuie sur A pour rejouer ou Q pour quitter", black)
            
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.x = 250
                        self.y = 250
                        self.body = []
                        self.length = 1
                        self.direction = [0, 0]
                        return
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()

    def eat(self, food):
        if self.x == food.x and self.y == food.y:
            food.x = round(random.randrange(0, screen_width - self.size) / self.size) * self.size
            food.y = round(random.randrange(0, screen_height - self.size) / self.size) * self.size
            self.length += 1

    def obstacle(self, obstacle):
        if self.x == obstacle.x and self.y == obstacle.y:
            obstacle.x = round(random.randrange(0, screen_width - self.size) / self.size) * self.size
            obstacle.y = round(random.randrange(0, screen_height - self.size) / self.size) * self.size
            self.length -= 2

class Food:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

    def draw(self):
        pygame.draw.rect(screen, cyan, [self.x, self.y, self.size, self.size])

class Obstacle:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

    def draw(self):
        pygame.draw.rect(screen, 'red', [self.x, self.y, self.size, self.size])

class Score:
    def __init__(self, score):
        self.score = score

    def draw(self):
        value = font_style.render(f"Score : {str(self.score)}", True, yellow)
        screen.blit(value, [0, 0])
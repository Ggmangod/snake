# game.py
import pygame
import random
from snake import Snake

class SnakeGame:
    def __init__(self):
        pygame.init()

        self.dis_width = 600
        self.dis_height = 400
        self.dis = pygame.display.set_mode((self.dis_width, self.dis_height))
        pygame.display.set_caption('Наша с Арланом змейка с БД')

        self.clock = pygame.time.Clock()

        self.snake_block = 10
        self.snake_speed = 15

        self.font_style = pygame.font.SysFont(None, 30)

        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (213, 50, 80)
        self.green = (0, 255, 0)
        self.blue = (50, 153, 213)

    def run(self):
        game_over = False
        game_close = False

        x1 = self.dis_width / 2
        y1 = self.dis_height / 2

        x1_change = 0
        y1_change = 0

        snake = Snake(self.dis, self.snake_block, self.green)
        food = self.spawn_food()

        while not game_over:

            while game_close:
                self.dis.fill(self.black)
                self.message("Вы проиграли. Если понравилось, нажмите C, чтобы сыграть снова. Q - выход", self.red)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            self.run()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -self.snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = self.snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -self.snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = self.snake_block
                        x1_change = 0

            if x1 >= self.dis_width or x1 < 0 or y1 >= self.dis_height or y1 < 0:
                game_close = True
            x1 += x1_change
            y1 += y1_change
            self.dis.fill(self.black)
            pygame.draw.rect(self.dis, self.green, [food[0], food[1], self.snake_block, self.snake_block])
            
            snake.move(x1, y1)
            snake.draw()

            pygame.display.update()

            if x1 == food[0] and y1 == food[1]:
                food = self.spawn_food()
                snake.grow()

            if snake.check_collision():
                game_close = True

            self.clock.tick(self.snake_speed)

        pygame.quit()
        quit()

    def spawn_food(self):
        foodx = round(random.randrange(0, self.dis_width - self.snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, self.dis_height - self.snake_block) / 10.0) * 10.0
        return [foodx, foody]

    def message(self, msg, color):
        mesg = self.font_style.render(msg, True, color)
        self.dis.blit(mesg, [self.dis_width / 6, self.dis_height / 3])

import pygame

class Snake:
    def __init__(self, display, block_size, color):
        self.display = display
        self.block_size = block_size
        self.color = color

        self.snake_list = []
        self.length = 1

    def move(self, x, y):
        self.snake_list.append([x, y]) 
        if len(self.snake_list) > self.length:
            del self.snake_list[0]

    def draw(self):
        for segment in self.snake_list:
            pygame.draw.rect(self.display, self.color, [segment[0], segment[1], self.block_size, self.block_size])

    def grow(self):
        self.length += 1

    def check_collision(self):
        head = self.snake_list[-1]
        for segment in self.snake_list[:-1]:
            if segment == head:
                return True
        return False

# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
    # print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


import pygame
import random


class Cube:
    width = 500
    cols = 20

    def __init__(self, position, color):
        self.position = position
        self.color = color
        self.dir_x = 1
        self.dir_y = 0

    def draw(self, surface):
        size_between = self.width // self.cols

        i = self.position[0]
        j = self.position[1]

        pygame.draw.rect(surface, self.color, (i * size_between + 1, j * size_between + 1, size_between - 1, size_between - 1))

    def move(self, dir_x, dir_y):
        self.dir_x = dir_x
        self.dir_y = dir_y
        self.position = (self.position[0] + self.dir_x, self.position[1] + self.dir_y)


class Snake:
    color = (0, 255, 55)
    body = []
    turns = {}

    def __init__(self, position):
        self.head = Cube(position, self.color)
        self.body.append(self.head)
        self.dir_x = 1
        self.dir_y = 0

    def draw(self, surface):
        for cube in self.body:
            cube.draw(surface)

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            dir_x = 0
            dir_y = 0

            for key in keys:
                if keys[pygame.K_LEFT]:
                    dir_x = -1
                    dir_y = 0
                elif keys[pygame.K_UP]:
                    dir_x = 0
                    dir_y = -1
                elif keys[pygame.K_RIGHT]:
                    dir_x = 1
                    dir_y = 0
                elif keys[pygame.K_DOWN]:
                    dir_x = 0
                    dir_y = 1
                if self.dir_x + dir_x != 0 and self.dir_y + dir_y != 0:
                    self.dir_x = dir_x
                    self.dir_y = dir_y
                    self.turns[self.head.position[:]] = [self.dir_x, self.dir_y]
        for index, cube in enumerate(self.body):
            position = cube.position[:]
            if position in self.turns:
                turn = self.turns[position]
                cube.move(turn[0], turn[1])
                if index == len(self.body) - 1:
                    self.turns.pop(position)
            else:
                if cube.dir_x == -1 and cube.position[0] <= 0:
                    cube.position = (cube.cols - 1, cube.position[1])
                elif cube.dir_y == -1 and cube.position[1] <= 0:
                    cube.position = (cube.position[0], cube.cols - 1)
                elif cube.dir_x == 1 and cube.position[0] >= cube.cols - 1:
                    cube.position = (0, cube.position[1])
                elif cube.dir_y == 1 and cube.position[1] >= cube.cols - 1:
                    cube.position = (cube.position[0], 0)
                else:
                    cube.move(cube.dir_x, cube.dir_y)


def snack(cols, snake):
    positions = snake.body

    while True:
        x = random.randrange(cols)
        y = random.randrange(cols)

        if len(list(filter(lambda z: z.position == (x, y), positions))) > 0:
            continue
        else:
            break

    return x, y


def draw_board(surface, snake, apple):
    surface.fill((55, 55, 55))
    snake.draw(surface)
    apple.draw(surface)
    pygame.display.update()


def main():
    width = 500
    height = 500
    cols = 20

    board = pygame.display.set_mode((width, height))
    snake = Snake((10, 10))
    apple = Cube(snack(cols, snake), color=(255, 55, 0))

    flag = True
    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(150)
        clock.tick(10)
        snake.move()

        draw_board(board, snake, apple)


if __name__ == '__main__':
    main()

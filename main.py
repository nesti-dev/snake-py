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


def draw_board(surface, snake):
    surface.fill((55, 55, 55))
    snake.draw(surface)
    pygame.display.update()


def main():
    width = 500
    height = 500
    rows = 20

    board = pygame.display.set_mode((width, height))
    snake = Snake((10, 10))

    flag = True
    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(150)
        clock.tick(10)

        draw_board(board, snake)


if __name__ == '__main__':
    main()

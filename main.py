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


def draw_board(width, rows, surface):
    surface.fill((0, 0, 0))
    pygame.display.update()


def main():
    width = 500
    height = 500
    rows = 20

    board = pygame.display.set_mode((width, height))

    flag = True
    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(150)
        clock.tick(10)

        draw_board(width, rows, board)


if __name__ == '__main__':
    main()

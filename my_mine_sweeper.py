import random

def main():
    LENGTH = 10
    WIDTH = 10
    MINE = 4

    field = create_field(LENGTH, WIDTH, MINE)

    print_initial_field(LENGTH, WIDTH)

    game(LENGTH, WIDTH, MINE, field)

def create_field(length, width, mine):
    field = [[0] * length for _ in range(width)]
    for i in range(mine):
        field[random.randrange(width)][random.randrange(length)] = 9

    for i in range(width):
        for j in range(length):
            if field[i][j] == 9:
                for ii in range(i - 1, i + 2):
                    for jj in range(j - 1, j + 2):
                        if (0 <= ii < width and 0 <= jj < length
                            and field[ii][jj] != 9):
                            field[ii][jj] += 1
    return(field)

def print_upper_border_of_field(length, width):
    print(' ' * (len(str(width)) + 2), end='')
    border = 0
    for j in range(length):
        print(j + 1, end='')
        if (j + 1) != length:
            print(' ', end='')
        border += (len(str(j + 1)) + 1)
    print("")
    print(' ' * (len(str(width)) + 1), end='')
    print('-'*(border + 1))
    return(border)

def print_left_border_of_field(i, width):
    print(i + 1, end=' ')
    if len(str(i + 1)) < len(str(width)):
        print(' ' * (len(str(width)) - len(str(i + 1))), end='')
    print('|', end='')

def print_bottom_border_of_field(width, border):
    print(' ' * (len(str(width)) + 1), end='')
    print('-'*(border + 1))

def print_initial_field(length, width):
    border = print_upper_border_of_field(length, width)

    for i in range(width):
        print_left_border_of_field(i, width)

        for j in range(length):
            print(' ' * len(str(j + 1)), end='')
            if (j + 1) != length:
                print(' ', end='')
        print('| ')

    print_bottom_border_of_field(width, border)

def print_lost_field(length, width, field):
    border = print_upper_border_of_field(length, width)

    for i in range(width):
        print_left_border_of_field(i, width)
        for j in range(length):
            if field[i][j] < 0:
                field[i][j] = -field[i][j] + 1
            if field[i][j] == 9:
                print('*', end='')
                print(' ' * (len(str(j + 1)) - 1), end='')
                if (j + 1) != length:
                    print(' ', end='')
            elif field[i][j] == 0:
                print(' ' * len(str(j + 1)), end='')
                if (j + 1) != length:
                    print(' ', end='')
            else:
                print(field[i][j], end='')
                print(' ' * (len(str(j + 1)) - len(str(field[i][j]))), end='')
                if (j + 1) != length:
                    print(' ', end='')
        print('| ')

    print_bottom_border_of_field(width, border)

def print_playing_filed(length, width, field):
    border = print_upper_border_of_field(length, width)

    for i in range(width):
        print_left_border_of_field(i, width)
        for j in range(length):
            if field[i][j] >= 0:
                print(' ' * len(str(j + 1)), end='')
                if (j + 1) != length:
                    print(' ', end='')
            elif field[i][j] == -1:
                print('_', end='')
                print(' ' * (len(str(j + 1)) - 1), end='')
                if (j + 1) != length:
                    print(' ', end='')
            else:
                print(-field[i][j] - 1, end='')
                print(' ' * (len(str(j + 1)) - len(str(-field[i][j] - 1))), end='')
                if (j + 1) != length:
                    print(' ', end='')
        print('| ')

    print_bottom_border_of_field(width, border)

def game(length, width, mine, field):
    closed = length * width - mine

    while closed:
        user_step = input('Input new step: ')
        parts = user_step.split()
        i = int(parts[0]) - 1
        j = int(parts[1]) - 1

        if field[i][j] == 9:
            print('Game over!')
            print_lost_field(length, width, field)
            break
        if field[i][j] < 0:
            continue

        if field[i][j] == 0:
            check_pos = [(i, j)]
            while check_pos:
                last = check_pos.pop()
                ci = last[0]
                cj = last[1]
                if 0 <= ci < 10 and 0 <= cj < 10:
                    if field[ci][cj] == 0:
                        check_pos.extend((ii, jj)
                                         for ii in range(ci-1, ci + 2)
                                         for jj in range(cj-1, cj+2)
                                         if not (ci == ii and cj == jj))
                    if field[ci][cj] >= 0:
                        field[ci][cj] = -field[ci][cj] - 1
                        closed -= 1
            print_playing_filed(length, width, field)
            continue

        field[i][j] = -field[i][j] - 1
        closed -= 1

        print_playing_filed(length, width, field)
    else:
        print('Winner!')

if __name__ == '__main__':
    main()

import re

WIDTH = 50
HEIGHT = 6

matrix = [[0 for j in range(WIDTH)] for i in range(HEIGHT)] 

rect_pattern = r'rect ([0-9]+)x([0-9]+)'
rotate_row_pattern = r'rotate row y=([0-9]+) by ([0-9]+)'
rotate_col_pattern = r'rotate column x=([0-9]+) by ([0-9]+)'


def rotate_row(row, steps):
    matrix[row] = matrix[row][-steps % WIDTH:] + matrix[row][:-steps % WIDTH]


def rotate_col(col, steps):
    column = []
    for i, j in enumerate(matrix):
        column.append(j[col])
    column_rotaded = column[-steps % HEIGHT:] + column[: -steps % HEIGHT]
    for i, val in enumerate(column_rotaded):
        matrix[i][col] = val


def rect(wide, tall):
    for i in range(tall):
        for j in range(wide):
            matrix[i][j] = 1


def follow_instruction(instruction):
    fill_rect = re.search(rect_pattern, instruction)
    rot_col = re.search(rotate_col_pattern, instruction)
    rot_row = re.search(rotate_row_pattern, instruction)

    if fill_rect:
        rect(int(fill_rect.group(1)), int(fill_rect.group(2)))
    elif rot_col:
        rotate_col(int(rot_col.group(1)), int(rot_col.group(2)))
    elif rot_row:
        rotate_row(int(rot_row.group(1)), int(rot_row.group(2)))
    else:
        print('Invalid instruction')

with open('day8.txt') as file:
    instruction_rows = file.readlines()
    for instruction in instruction_rows:
        follow_instruction(instruction)

cnt = 0
for l in matrix:
    print(l)
    for c in l:
        cnt += c
print(cnt)




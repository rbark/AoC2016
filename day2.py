from utils import utilitys

keypad = [[1,2,3],
          [4,5,6],
          [7,8,9]]

fancy_keypad = [['x','x','1','x','x'],
                ['x','2','3','4','x'],
                ['5','6','7','8','9'],
                ['x','A','B','C','x'],
                ['x','x','D','x','x']]



print(keypad[0][2])
current_row = 1
current_col = 1

instruction_rows = []

with open('day2.txt') as file:
    instruction_rows = file.readlines()

def move_up():
    global current_row
    if current_row != 0:
        current_row -= 1

def move_down():
    global current_row
    if current_row != 2:
        current_row += 1

def move_left():
    global current_col
    if current_col != 0:
        current_col -= 1

def move_right():
    global current_col
    if current_col != 2:
        current_col += 1



for line in instruction_rows:
    chars = list(line)
    for direction in chars:
        if direction == 'L':
            move_left()
        elif direction == 'R':
            move_right()
        elif direction == 'D':
            move_down()
        elif direction == 'U':
            move_up()
    print('row: ' + str(current_row) + ' col: ' +str(current_col) + ' and that is nummer: ' + str(keypad[current_row][current_col]))

import re

instructions = []
register = [0, 0, 1, 0]  # a b d d

jump_pattern = (r'jnz ([[\d|\D]+) ([\-]?\d+)')
modify_register_pattern = (r'(dec|inc) ([\d|\D]+)')
copy_pattern = (r'cpy (\D|\d+) (\D|\d+)')

with open("day12.txt") as f:
    for i, instruction in enumerate(f.readlines()):
        instructions.append(instruction.strip())

instructon_pointer = 0


def get_value(val):
    if val == 'a':
        return register[0]
    elif val == 'b':
        return register[1]
    elif val == 'c':
        return register[2]
    elif val == 'd':
        return register[3]
    else:
        return int(val)


def get_register(val):
    if val == 'a':
        return 0
    elif val == 'b':
        return 1
    elif val == 'c':
        return 2
    elif val == 'd':
        return 3
    else:
        return -1


while instructon_pointer < len(instructions):
    jump = re.match(jump_pattern, instructions[instructon_pointer])
    modify = re.match(modify_register_pattern, instructions[instructon_pointer])
    copy = re.match(copy_pattern, instructions[instructon_pointer])
    if jump:
        a = 1
        if get_value(jump.group(1)) != 0:
            instructon_pointer += int(jump.group(2))
            continue
    elif modify:
        if modify.group(1) == 'inc':
            register[get_register(modify.group(2))] += 1
        else:
            register[get_register(modify.group(2))] -= 1
    elif copy:
        val = get_value(copy.group(1))
        register[get_register(copy.group(2))] = val
    else:
        print('fail on: ' + instructions[instructon_pointer])
    instructon_pointer += 1


print(register)
#9227663
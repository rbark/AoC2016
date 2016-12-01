from utils import utilitys

puzzle = 'L1, R3, R1, L5, L2, L5, R4, L2, R2, R2, L2, R1, L5, R3, L4, L1, L2, R3, R5, L2, R5, L1, R2, L5, R4, R2, R2, L1, L1, R1, L3, L1, R1, L3, R5, R3, R3, L4, R4, L2, L4, R1, R1, L193, R2, L1, R54, R1, L1, R71, L4, R3, R191, R3, R2, L4, R3, R2, L2, L4, L5, R4, R1, L2, L2, L3, L2, L1, R4, R1, R5, R3, L5, R3, R4, L2, R3, L1, L3, L3, L5, L1, L3, L3, L1, R3, L3, L2, R1, L3, L1, R5, R4, R3, R2, R3, L1, L2, R4, L3, R1, L1, L1, R5, R2, R4, R5, L1, L1, R1, L2, L4, R3, L1, L3, R5, R4, R3, R3, L2, R2, L1, R4, R2, L3, L4, L2, R2, R2, L4, R3, R5, L2, R2, R4, R5, L2, L3, L2, R5, L4, L2, R3, L5, R2, L1, R1, R3, R3, L5, L2, L2, R5'
puzzle_1 = 'R7, R2, R3, R4'

horizontal = 0
vertical = 0
coordinates = {"0:0"}  # x, y
current_direction = 'N'
step_number = 0
crossed = False
cross_point = ""

print(utilitys.get_word_array(puzzle))

directions = utilitys.get_word_array(puzzle)


def move_santa(direction_instruction):
    global horizontal
    global vertical
    global current_direction
    global crossed
    global coordinates
    global cross_point
    direction = direction_instruction[:1]
    distance = int(direction_instruction[1:])

    if current_direction == 'N':
        if direction == 'L':
            current_direction = 'W'
            if not crossed:
                for i in range(1, distance + 1):
                    coord = str(horizontal - i) + ":" + str(vertical)
                    print(coord)
                    if coord in coordinates:
                        crossed = True
                        cross_point = coord
                    else:
                        coordinates.add(coord)
            horizontal -= distance
        else:
            current_direction = 'E'
            if not crossed:
                for i in range(1, distance + 1):
                    coord = str(horizontal + i) + ":" + str(vertical)
                    print(coord)
                    if coord in coordinates:
                        crossed = True
                        cross_point = coord
                    else:
                        coordinates.add(coord)
            horizontal += distance
    elif current_direction == 'S':
        if direction == 'L':
            current_direction = 'E'
            if not crossed:
                for i in range(1, distance + 1):
                    coord = str(horizontal + i) + ":" + str(vertical)
                    print(coord)
                    if coord in coordinates:
                        crossed = True
                        cross_point = coord
                    else:
                        coordinates.add(coord)
            horizontal += distance
        else:
            current_direction = 'W'
            if not crossed:
                for i in range(1, distance + 1):
                    coord = str(horizontal - i) + ":" + str(vertical)
                    print(coord)
                    if coord in coordinates:
                        crossed = True
                        cross_point = coord
                    else:
                        coordinates.add(coord)
            horizontal -= distance
    elif current_direction == 'E':
        if direction == 'L':
            current_direction = 'N'
            if not crossed:
                for i in range(1, distance + 1):
                    coord = str(horizontal) + ":" + str(vertical + i)
                    print(coord)
                    if coord in coordinates:
                        crossed = True
                        cross_point = coord
                    else:
                        coordinates.add(coord)
            vertical += distance
        else:
            current_direction = 'S'
            if not crossed:
                for i in range(1, distance + 1):
                    coord = str(horizontal) + ":" + str(vertical - i)
                    print(coord)
                    if coord in coordinates:
                        crossed = True
                        cross_point = coord
                    else:
                        coordinates.add(coord)
            vertical -= distance
    else:
        if direction == 'L':
            current_direction = 'S'
            if not crossed:
                for i in range(1, distance + 1):
                    coord = str(horizontal) + ":" + str(vertical-i)
                    print(coord)
                    if coord in coordinates:
                        crossed = True
                        cross_point = coord
                    else:
                        coordinates.add(coord)
            vertical -= distance
        else:
            current_direction = 'N'
            if not crossed:
                for i in range(1, distance + 1):
                    coord = str(horizontal) + ":" + str(vertical+i)
                    print(coord)
                    if coord in coordinates:
                        crossed = True
                        cross_point = coord
                    else:
                        coordinates.add(coord)
            vertical += distance


for direction_to_go in directions:
    print(direction_to_go)
    start_x = horizontal
    start_y = vertical
    move_santa(direction_to_go)
    print("new pos vert:" + str(vertical) + " and hor:" + str(horizontal))

print("tot: " + str(abs(horizontal) + abs(vertical)))
print("kryss: " + cross_point)

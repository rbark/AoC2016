import re

rooms = []

def get_checksum(room):
    counts = {}
    for char in room:
        if char in counts.keys():
            counts[char] += 1
        else:
            counts[char] = 1

    checksum = ''

    for i in range(max(counts.values()), 0, -1 ):
        chars = ''
        for char, val in counts.items():
            if val == i:
                chars += char

        checksum +=  ''.join(sorted(chars))
    return checksum[:5]

with open('day4.txt') as file:
    rooms = file.readlines()


parts = re.compile(r'([a-z-]+)(\d+)\[(.+)\]')

id_sum = 0

for room in rooms:
    room_parts = re.split(parts, room)
    if room_parts[3] == get_checksum(room_parts[1].replace('-' , '')):
        id_sum += int(room_parts[2])

print('Sum is ' + str(id_sum))

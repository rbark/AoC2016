import re

rooms = []

def get_checksum(room):
    counts = {}
    for char in room.replace('-' , ''):
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

def decrypt(c, number):
    if c == '-':
        return ' '
    else:
        x = ord(c) - ord('a')
        return chr((x + number) % 26 + ord('a'))

with open('day4.txt') as file:
    rooms = file.readlines()


parts = re.compile(r'([a-z-]+)(\d+)\[(.+)\]')

id_sum = 0

print(decrypt('a', 105))

for room in rooms:
    room_parts = re.split(parts, room)
    if room_parts[3] == get_checksum(room_parts[1]):
        roomname= ''
        for c in room_parts[1]:
            roomname += ''.join(decrypt(c, int(room_parts[2])))
        if 'north' in roomname:
            print(roomname + ': ' + room_parts[2])
        id_sum += int(room_parts[2])

print('Sum is ' + str(id_sum))

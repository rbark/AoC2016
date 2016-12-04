import re

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

    print('checksum is : ' + checksum)



splitparts = re.compile(r'([a-z-]+)(\d+)\[(.+)\]')
teststr = 'aaaaa-bbb-z-y-x-123[abxyz]'
testa = re.split(splitparts, teststr)
#print(str(testa))
print(testa)

get_checksum('abcddefffgggghhi')
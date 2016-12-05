import hashlib

s = hashlib.md5("abc5017308".encode('utf-8')).hexdigest()

position_set = set()
startkey = 'uqwqemis'
count = 0
number_str = ''
chars = ['', '', '', '', '', '', '', '']

while len(position_set) != 8:
    s = str(hashlib.md5((str(startkey) + str(count)).encode('utf-8')).hexdigest())
    if s[:5] == str('00000'):
        if s[5:6].isdigit() and int(s[5:6]) < 8:
            if s[5:6] not in position_set:
                position_set.add(s[5:6])
                chars[int(s[5:6])] = s[6:7]
    count += 1

answer = ''
for c in chars:
    answer += c
print(answer)

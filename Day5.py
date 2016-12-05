import hashlib

s = hashlib.md5("abc5017308".encode('utf-8')).hexdigest()

startkey = 'uqwqemis'
count = 0
number_str = ''

while len(number_str) != 8 :
    s = str(hashlib.md5((str(startkey) + str(count)).encode('utf-8')).hexdigest())
    if s[:5] == str('00000'):
        number_str += number_str.join(s[5:6])
    count += 1
print(number_str)
import re
compressed_words = []
instruction_pattern = re.compile(r'\(([0-9]+)x([0-9]+)\)')

with open("day9.txt") as f:
    for line in f.readlines():
        compressed_words.append(line.strip())

def unzip(word):
    i = 0
    cnt = 0
    while i < len(word):
        match = instruction_pattern.match(word, i)
        if match:
            start = match.end(0)
            end = int(match.group(1)) + start
            to_repeat = word[start:end]
            cnt = cnt + unzip(to_repeat) * int(match.group(2))
            i = end
        else:
            i = i + 1
            cnt = cnt +1
    return cnt


print(unzip(compressed_words[0].strip()))
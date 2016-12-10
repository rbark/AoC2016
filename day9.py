
compressed_words = []

with open("day9.txt") as f:
    for line in f.readlines():
        compressed_words.append(line.strip())

i = 0
ans = ''
tot = 0
for compressed_word in compressed_words:
    print(compressed_word)
    n = len(compressed_word)
    while i < n:
        c = compressed_word[i]
        if c != '(':
            ans += c
            i += 1
        else:
            decompress_instruction = ''
            i += 1
            while compressed_word[i] != ')':
                decompress_instruction += compressed_word[i]
                i += 1
            letters, times = map(int, decompress_instruction.split('x'))
            i += 1
            string = compressed_word[i:i + letters]
            ans += string * times
            i += letters
    tot += len(ans)
print(str(tot))
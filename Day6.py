letter_freq = [{} for i in range(8)]  # array with 8 dicts

with open('day6.txt') as file:
    instruction_rows = file.readlines()
    for word_count, word in enumerate(instruction_rows):
        # print(str(word_count) + ': ' + word)
        for i, c in enumerate(word.strip()):
            if c in letter_freq[i].keys():
               letter_freq[i][c] += 1
            else:
               letter_freq[i][c] = 1

max_string = ''
min_string = ''

for i in range(8):
    for c, val in letter_freq[i].items():
        if val == max(letter_freq[i].values()):
            max_string += c
        if val == min(letter_freq[i].values()):
            min_string += c

print(max_string)
print(min_string)


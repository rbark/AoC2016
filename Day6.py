
with open('day6.txt') as file:
    instruction_rows = file.readlines()

col1 = []
col2 = []
col3 = []
col4 = []
col5 = []
col6 = []
col7 = []
col8 = []

def put_letters_to_array(word):
    col1.append(word[0])
    col2.append(word[1])
    col3.append(word[2])
    col4.append(word[3])
    col5.append(word[4])
    col6.append(word[5])
    col7.append(word[6])
    col8.append(word[7])

def max_chars(word):
    counts = {}
    for char in word:
        if char in counts.keys():
            counts[char] += 1
        else:
            counts[char] = 1


    max_val = max(counts.values())

    for c, val in counts.items():
        if val == max_val:
            return c



sec_word = ''
for line in instruction_rows:
    put_letters_to_array(line)

sec_word += max_chars(col1)
sec_word += max_chars(col2)
sec_word += max_chars(col3)
sec_word += max_chars(col4)
sec_word += max_chars(col5)
sec_word += max_chars(col6)
sec_word += max_chars(col7)
sec_word += max_chars(col8)

print( sec_word)
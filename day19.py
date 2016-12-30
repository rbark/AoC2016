from collections import deque

number_of_elfs = 3014603

elfs = deque(list(range(1, number_of_elfs+2)))

while len(elfs) > 1:
    first = elfs.popleft()
    elfs.popleft()
    elfs.append(first)

print(elfs.popleft())
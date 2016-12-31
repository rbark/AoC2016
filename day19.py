from collections import deque
import itertools

number_of_elfs = 3014603
# number_of_elfs = 5


# print(elfs)

def day1():
    elfs = deque(list(range(1, number_of_elfs + 1)))
    while len(elfs) > 1:
        first = elfs.popleft()
        elfs.popleft()
        elfs.append(first)
    print(elfs.popleft())


def day2():
    elfs = deque(list(range(1, number_of_elfs + 1)))

    elfs_left = deque(itertools.islice(elfs, 0, len(elfs) // 2))
    elfs_right = deque(itertools.islice(elfs, len(elfs) // 2, len(elfs) + 1))
    print(elfs_right)
    print(elfs_left)
    while elfs_left and elfs_right:
        if len(elfs_left) > len(elfs_right):
            elfs_left.pop()
        else:
            elfs_right.pop()

        elfs_right.appendleft(elfs_left.popleft())
        elfs_left.append(elfs_right.pop())


    print(elfs_left)
    print(elfs_right)


# def day2():
#     elfs_left = deque(list(range(1, (number_of_elfs + 1)//2)))
#     elfs_right = deque(list(range((number_of_elfs + 1)//2 , number_of_elfs + 1)))
#     print(elfs_left)
#     print(elfs_right)
#     while elfs_left and elfs_right:
#         if len(elfs_right) > len(elfs_left):
#             print(elfs_right.popleft())
#         else:
#             print(elfs_left.pop())
#
#     print(elfs_left)
#     print(elfs_right)
# while len(elfs) > 1:
#     crossover_elf = number_of_elfs//2
#     elfs.rotate(crossover_elf)
#     # print(elfs)
#     # print(crossover_elf)
#     elfs.pop()
#     # print(elfs)
# print(elfs.pop())

day2()

import re

hypernet_pattern = '\[[a-z]*\]'


def get_parts(word):
    hypernets = re.findall(hypernet_pattern, word)
    net_groups = re.split('\[|\]', word)
    stand_net = []
    for net in net_groups:
        if '[' + net + ']' not in hypernets:
            stand_net.append(net)
    return stand_net, hypernets


def check_if_abba(word):
    i = 0
    while i < len(word) - 3:
        if word[i] == word[i + 3] and word[i] != word[i + 1] and word[i + 1] == word[i + 2]:
            return True
        i += 1
    return False


def valid_ip(hypernets, nets):
    for word in hypernets:
        if check_if_abba(word):
            return False
    for word in nets:
        if check_if_abba(word):
            return True
    return False



cnt = 0
with open('day7.txt') as file:
    rows = file.readlines()
    for word in rows:
        (nets , hypernets ) = get_parts(word)
        if valid_ip(hypernets, nets):
            cnt += 1
print(cnt)


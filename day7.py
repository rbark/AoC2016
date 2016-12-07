import re

hypernet_pattern = '\[[a-z]*\]'
cnt = 0
cnt2 = 0


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


def check_if_aba(word):
    i = 0
    words = []
    valid = False
    while i < len(word) - 2:
        if word[i] == word[i + 2] and word[i] != word[i + 1]:
            valid = True
            words.append( word[i] + word[i + 1] + word[i + 2])
        i += 1
    return valid, words


def valid_ip(nets, hypernets):
    for word in hypernets:
        if check_if_abba(word):
            return False
    for word in nets:
        if check_if_abba(word):
            return True
    return False


def valid_ip_aba(nets, hypernets):
    for word in nets:
        (valid, words) = check_if_aba(word)
        if valid:
            for word in words:
                word_to_find = word[1] + word[0] + word[1]
                for hypernet in hypernets:
                    if word_to_find in hypernet:
                        return True
    return False

with open('day7.txt') as file:
    rows = file.readlines()
    for word in rows:
        (nets, hypernets) = get_parts(word)
        if valid_ip(nets, hypernets):
            cnt += 1
        if valid_ip_aba(nets, hypernets):
            cnt2 += 1
print(cnt)
print(cnt2)

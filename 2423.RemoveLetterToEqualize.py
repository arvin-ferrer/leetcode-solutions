def freq(word):
    hashmap = {}
    frequencies = []
    for i in word:
        hashmap[i] = hashmap.get(i, 0)+1
    for value in hashmap.values():
        frequencies.append(value)
        nodups = list(set(frequencies))
    if len(nodups) > 2:
        return False
    copy = frequencies[:]
    for idx, i in enumerate(copy):
        frequencies[idx] -= 1
        if frequencies[idx] == 0:
            frequencies.pop(idx)
        if len(set(frequencies)) == 1:
            return True
        frequencies = copy[:]

    return False

print(freq("ddaccb"))

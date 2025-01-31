def isIsomorphic(s, t):
    mapping = {}
    if len(s) != len(t):
        return False
    for idx, i in enumerate(s):
        if i not in mapping:
            mapping[i] = t[idx]

    dups = []
    for value in mapping.values():
        dups.append(value)
    if len(dups) != len(set(dups)):
        return False 

    for idx, i in enumerate(s):
        if mapping[i] != t[idx]:
            return False
    return True

isIsomorphic("egg", "add")


def mismatch(s1, s2):
    mismatch = 0
    s1hashmap = {}
    s2hashmap = {}
    if s1 == s2:
        return True
    if len(s1) == len(s2):
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                s1hashmap[s1[i]] = i
                mismatch += 1
        for i in range(len(s2)):
            if s1[i] != s2[i]:
                s2hashmap[s2[i]] = i
    if mismatch > 2:
        return False
    for key in s1hashmap.keys():
        if key not in s2hashmap:
            return False 
    
    return True
#test case
mismatch("bank", "kanb")


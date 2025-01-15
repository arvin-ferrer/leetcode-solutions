

def bits(n):
    result = ""
    while n != 0:
        r = n %2
        n = n//2
        result = str(r) + result
    print(result)
    count = 0
    for i in result:
        if i == "1":
            count += 1
    print(count)
bits(11)

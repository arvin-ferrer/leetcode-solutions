def singleNumber(nums):
    x = {}
    for i in nums:
        x[i] = x.get(i, 0)+1
    for i, count in x.items():
        if count == 1:
            print(x)
            return i
singleNumber([2,2,1])

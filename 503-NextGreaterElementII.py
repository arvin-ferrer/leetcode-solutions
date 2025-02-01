def next(nums):
    circularArr = [*nums, *nums]
        # print(circularArr)
    output = []
    for i in range(len(circularArr)):
        subarr = circularArr[i: len(circularArr)]
        print(subarr)
        target = subarr[0]
        if len(subarr) == 1:
            output.append(-1)
        nolargest = False
        for j in range(1,len(subarr)):
            if subarr[j] > target:
                output.append(subarr[j])
                nolargest = False
                break
            elif subarr[j] <=  target:
                nolargest = True
                continue
        if nolargest:
            output.append(-1)    
    return output[0: len(nums)]   

next([1,1,1,1,1])
def next(nums1, nums2):
    output = []
    for j in nums1:
            
        current = nums2.index(j)
        subarr = nums2[current: len(nums2)]
        target = subarr[0]
        if len(subarr) == 1:
            output.append(-1)
        nolargest = False
        for i in range(1,len(subarr)):
            if subarr[i] > target:
                output.append(subarr[i])
                nolargest = False
                break
            elif subarr[i] < target:
                nolargest = True
                continue
        if nolargest:
            output.append(-1)

    return output 
next([1,3,5,2,4],[6,5,4,3,2,1,7])
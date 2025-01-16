
def twoSum(nums, target):
    for x in range(len(nums)):
        for y in range(x+1,len(nums)):
            if nums[x]+nums[y] == target: 
                return(x,y)
            else:
                continue
              


#add more testcases if you want
print(twoSum([2,7,11,15], 9))

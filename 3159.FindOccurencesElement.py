def findoccurences(nums, queries, x):
    output = []
    indices = []
    for idx, i in enumerate(nums):
        if i == x:
            indices.append(idx)

    for i in range(len(queries)):
        if queries[i] > len(indices):
            output.append(-1)
        else:
            output.append(indices[queries[i]-1])    
    return output

findoccurences([1,3,1,7], [1,3,2,4], 1)

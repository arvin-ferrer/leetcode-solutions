def prefix(A,B):
    output = []
    for i in range(len(A)):
        count = 0
        subarr = A[0:i+1]
        for i in range(i+1):
            if B[i] in subarr:
                count += 1
        output.append(count)
    return output
prefix([1,3,2,4],[3,1,2,4])

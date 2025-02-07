def matrix(matrix):
    indicesRow = []
    indicesCol = []
    for idx, i in enumerate(matrix):
        for jdx, j in enumerate(i):
            if j == 0:
                indicesRow.append(idx)
                indicesCol.append(jdx)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i in indicesRow or j in indicesCol:
                matrix[i][j] = 0
            
    return matrix
print(matrix([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))

def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
    result = []
    
    for i in range(len(a)):
        if len(a[i]) != len(b):
            return -1
        
        res = 0    

        for y in range(len(a[i])):
            res += a[i][y] * b[y]

        result.append(res) 


    return result

print(matrix_dot_vector([[1,2],[2,4]], [1,2]))
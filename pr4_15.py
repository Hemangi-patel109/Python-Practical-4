#Write a Python program to add two matrices.

def add_matrices(mat1, mat2):
    row1 = len(mat1)
    col1 = len(mat1[0]) if row1 > 0 else 0
    row2 = len(mat2)
    col2 = len(mat2[0]) if row2 > 0 else 0
    
    if row1 != row2 or col1 != col2:
        print("None")
    result_mat = []
    for i in range(row1):
        row = []
        for j in range(col1):
            row.append(mat1[i][j] + mat2[i][j])
        result_mat.append(row)
    return result_mat

matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
matrix2 = [[1,2,3],[4,5,6],[7,8,9]]
print(f"Matrix1: {matrix1}")
print(f"Matrix1: {matrix2}")
print(add_matrices(matrix1, matrix2))  
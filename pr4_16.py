#Write a Python program to transpose a given matrix.

def trans_mat(matrix):
    rows = len(matrix)
    if rows == 0:
        return []
    cols = len(matrix[0])
    for row in matrix:
        if len(row) != cols:
            return "Rows have different lengths."

    trans_mat = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        trans_mat.append(new_row)
    return trans_mat

matrix1 = [[1,2,3],[4,5,6],[7,8,9]]

trans_mat1 = trans_mat(matrix1)
if trans_mat1:
    print("Original Matrix:")
    for row in matrix1:
        print(row)
    print("Transposed Matrix:")
    for row in trans_mat1:
        print(row)
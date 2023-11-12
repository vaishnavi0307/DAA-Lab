## Q1 - INTERCHANGING DIAGONALS

# Interchange the Diagonal

#  0 1 2                        2 1 0
#  3 4 5    ---------------->   3 4 5
#  6 7 8                        8 7 6

# Input : [0, 4, 8] is the LEFT diagonal & [2, 4, 6] is the RIGHT diagonal
# Output : [0, 4, 8] is the RIGHT diagonal & [2, 4, 6] is the LEFT diagonal

# Trick : Swap the corners

def interchange_diagonals(matrix):
    n = len(matrix)          # len(matrix) gives the number of rows in the matrix i.e., n = 3
    for i in range(n):
        matrix[i][i], matrix[i][n-i-1] = matrix[i][n-i-1], matrix[i][i]   # Swapping the corners
        # since we are representing the no.s & matrix in the form of array, the indexing starts from 0, 1, 2...
    return matrix

original_matrix = [[0, 1, 2], 
                   [3, 4, 5], 
                   [6, 7, 8]]
result_matrix = interchange_diagonals(original_matrix)

for row in result_matrix:
    print(row)

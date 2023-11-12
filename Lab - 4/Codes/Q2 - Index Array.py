## Q2 - INDEX ARRAY

# Display the index no. in the array by finding that number in the array

# A[i] = i

def index_array(A):
    n = len(A)
    
    for i in range(n): 
        while A[i] != i:               # != - not equal to
            temp = A[i]
            A[i], A[temp] = A[temp], A[i]
    return A

A = [2, 3, 1, 0, 4, 5, 7, 6, 9, 8]
result = index_array(A)
print(result)

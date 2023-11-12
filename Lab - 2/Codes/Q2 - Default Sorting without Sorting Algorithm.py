## Q2 - DEFAULT SORT WITHOUT ANY INSERTING ALGORITHM

# Given array : [0, 0, 1, 2, 0, 1, 2, 2, 1]
# Output : [0, 0, 0, 1, 1, 1, 2, 2, 2]

# Sorting using  

def default_sort(a):
    n = len(a)       # Length of the Array

    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place, so we don't need to check them again
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]      # Here no.s are swapped

# Input array
a = [0, 0, 1, 2, 0, 1, 2, 2, 1]

# Call the custom_sort function to sort the array
default_sort(a)

# Display the sorted array
print("Sorted Array : ", a)

# Time Complexity : n^2

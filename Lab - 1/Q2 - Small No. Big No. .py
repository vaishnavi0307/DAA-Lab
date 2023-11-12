## Q2 - SORTING IN SMALL NUMBER & BIG NUMBER MANNER

## Sorting in Small Number & Big Number Manner

# Input - Array
# Output - Small No. , Big No. , .....

def SmallNoBigNo(arr, n):                                 # Zig Zag Numbers
    arr.sort()                                            # using sort function to sort the array
    for i in range(1, n-1, 2):                            # traverse the array from 1 to n-1
        arr[i], arr[i+1] = arr[i+1], arr[i]               # swap value of current element with next element
    print(arr)


if __name__ == "__main__":
    arr = [4, 3, 7, 8, 6, 2, 1]
    n = len(arr)
    SmallNoBigNo(arr, n)

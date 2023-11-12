## Q3 - MERGE SORT

# Merge Sort

# Time Complexity : N log N

# Normal while loop where i, i, i = N
# if there is patterns like i/2 = log N
# if there is a loop i and then another loop in it i.e., iteration or is there is while loop = N log N

def merge_sort(arr, start, end):
    
    if start < end:                
# start < end, thsi is due to if there is a single element in the array, 
# starting index = ending index and then if there is a single element, there is nothing to sort in the array.
# So, to avoid that condition we make sure starting index is less than ending index
        mid = (start + end) // 2

        # Sort the first/left half
        merge_sort(arr, start, mid)

        # Sort the second half
        merge_sort(arr, mid + 1, end)

        # Merge the two sorted halves
        merge(arr, start, mid, end)

def merge(arr, start, mid, end):
    left_half = arr[start:mid + 1]
    right_half = arr[mid + 1:end + 1]

    i = j = 0
    k = start

    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

# Example Usage
arr = list(map(int, input("Enter space-separated numbers in the array: ").split()))
merge_sort(arr, 0, len(arr) - 1)
print(arr)

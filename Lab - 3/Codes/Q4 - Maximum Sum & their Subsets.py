## Q4 - MAXIMUM SUM & THEIR SUBSETS

def find_max_sum_subsets(arr):
    n = len(arr)
    max_sum = float("-inf")
    max_subsets = []

    # Generate all possible subsets of the array
    for i in range(1 << n):
        subset = [arr[j] for j in range(n) if (i & (1 << j)) > 0]

        # Calculate the sum of the current subset
        current_sum = sum(subset)

        # Check if the current sum is greater than the maximum sum
        if current_sum > max_sum:
            max_sum = current_sum
            max_subsets = [subset]
        elif current_sum == max_sum:
            max_subsets.append(subset)

    return max_sum, max_subsets

# Example usage
user_input = input("Enter the array elements separated by spaces: ")
arr = list(map(int, user_input.split()))
max_sum, max_subsets = find_max_sum_subsets(arr)

print("Maximum Sum:", max_sum)
print("Different Possible Element Sets:")
for subset in max_subsets:
    print(subset)

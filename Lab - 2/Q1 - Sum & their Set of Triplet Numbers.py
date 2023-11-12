## Q1 - SUM & THEIR SET OF TRIPLET NUMBERS

# Triplet Numbers and their Sum

# Ex : 

## A = [1, 2, 3, 4, 5]

# Sum needs to be 9 ; add any three no.s from the above array, their sum needs to 9

# 2 + 3 + 5 = 9
# 1 + 3 + 5 = 9 

# 1 Loop

# Time Complexity = n (since only 1 loop)

def find_triplets_with_sum(arr, target_sum):
    n = len(arr)
    found_triplets = []

    # Sort the array for better efficiency
    arr.sort()

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:                                       
            # whule loop is only for condition checking.... it doesnt stay till the end
            current_sum = arr[i] + arr[left] + arr[right]

            if current_sum == target_sum:
                found_triplets.append((arr[i], arr[left], arr[right]))
                left += 1
                right -= 1
            elif current_sum < target_sum:
                left += 1
            else:
                right -= 1

    return found_triplets

# Example usage:
user_sum = int(input("Enter the target sum: "))
user_array = list(map(int, input("Enter space-separated numbers in the array: ").split()))

triplets = find_triplets_with_sum(user_array, user_sum)

if triplets:
    print("Triplets with the sum", user_sum, "are:")
    for triplet in triplets:
        print(triplet)
else:
    print("No triplets found with the given sum.")

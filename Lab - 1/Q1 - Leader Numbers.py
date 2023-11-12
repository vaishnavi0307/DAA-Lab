## Q1 - LEADING NUMBERS

## Leader Numbers : In the array, considering the right numbers, we need to check if left number is 
# biggest than the right side numbers

## In a given array, we need to extract the greatest elements if the numbers after them are smaller than that number

def leader_numbers(arr):
    n = len(arr)                     # len(arr) givens the no. of elements of the array
    leaders = [ ]
    max_right = arr[n - 1]           # Displays (n-1)th index of the array since index starts from 0 to n
    
    leaders.append(max_right)        # Rightmost or last element of the array is the leader number always 
                                     # because there are no numbers after it to compare
    for i in range(n - 2, -1, -1) :
        if arr[i] > max_right: 
            max_right = arr[i]
            leaders.append(max_right)
        
    return leaders[::-1]
    
sample = [16, 17, 4, 3, 5, 2]
result = leader_numbers(sample)
print("Leader Numbers : ", result)      

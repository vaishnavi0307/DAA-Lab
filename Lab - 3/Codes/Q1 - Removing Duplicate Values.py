## Q1 - REMOVING DUPLICATE VALUES

def remove_dup_values(input_list):
    output_list = []
    for item in input_list:
        if item not in output_list:
            output_list.append(item)
    return output_list

user_input = input("Enter a list of numbers separated by commas: ")
user_list = [int(x) for x in user_input.split(',')]

result_list = remove_dup_values(user_list)

print("Original List:", user_list)
print("List with Duplicates Removed:", result_list)

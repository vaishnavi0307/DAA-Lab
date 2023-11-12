## Q2 - MULTIPLICATION OF NUMBERS WITHOUT IN-BUILT FUNCTIONS

# Multiply 2 integers
# DO NOT USE multiplication, division, for loops, bitwise operators
# Can be done using Recursion

def multiplication(a, b):
    if b == 0:
        return 0
    return a + multiplication(a, b - 1)   # Recursion 

a = int(input("Enter 1st Integer : "))
b = int(input("Enter 2nd Integer : "))

result = multiplication(a,b)
print("Product: ", result)

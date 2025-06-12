# find the maximum of three numbers using functions
def max_of_three(r, s, t):
    return max(r, s, t)

print(max_of_three(20, 500, 80))
# Output: 500

# Function of reverse a string
def reverse_string(s):
    return s[::-1]

text = "Hollywood"
print(reverse_string(text))
# Output: doowylloH

# print squares of numbers from 1 to 30
squares = [i**2 for i in range(1, 31)]
print(squares)
# Output [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900]

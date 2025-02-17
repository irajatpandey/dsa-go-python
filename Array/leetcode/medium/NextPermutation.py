#https://leetcode.com/problems/next-permutation/description/

def next_permutation(nums):
    # Function implementation goes here
    pass

# Test cases
test_cases = [
    [1, 2, 3],
    [3, 2, 1],
    [1, 1, 5],
    [1, 3, 2]
]

for i, nums in enumerate(test_cases, 1):
    print(f"Test Case {i}: Before: {nums}", end=", ")
    next_permutation(nums)
    print(f"After: {nums}")

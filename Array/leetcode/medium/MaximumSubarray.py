# https://leetcode.com/problems/maximum-subarray/description/
def max_sub_array(nums):
    # Implementation
    current_sum = 0
    max_sum = float('-inf')
    
    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

test_cases = [
    [-2, 1, -3, 4, -1, 2, 1, -5, 4],
    [1],
    [5, 4, -1, 7, 8],
    [-1, -2, -3, -4],
]

for i, nums in enumerate(test_cases, 1):
    result = max_sub_array(nums)
    print(f"Test Case {i}: {result}")
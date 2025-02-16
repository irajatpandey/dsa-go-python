#https://leetcode.com/problems/majority-element/description/
def majority_element(nums):
    # Implementation
    count = 0
    candidate = 0
    for item in nums:
        if count == 0:
           candidate = item
        elif candidate == item:
            count += 1
        else:
            count -= 1
    return candidate

test_cases = [
    [3, 2, 3],
    [2, 2, 1, 1, 1, 2, 2],
    [1],
    [6, 5, 5],
]

for i, nums in enumerate(test_cases, 1):
    result = majority_element(nums)
    print(f"Test Case {i}: {result}")

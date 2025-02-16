#https://leetcode.com/problems/two-sum/
def two_sum(nums, target):
    hash_map = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hash_map:
            return [hash_map[complement], i]
        hash_map[nums[i]] = i
    return []

test_cases = [
    ([2, 7, 11, 15], 9),
    ([3, 2, 4], 6),
    ([3, 3], 6),
]

for i, (nums, target) in enumerate(test_cases, 1):
    print(f"Test Case {i}:", two_sum(nums, target))

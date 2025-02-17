#https://leetcode.com/problems/rearrange-array-elements-by-sign/description/
def rearrangeArray(nums):
        positive = []
        negative  = []
        for item in nums:
            if item < 0:
                negative.append(item)
            else:
                positive.append(item)
        
        result = []
        for p, n in zip(positive, negative):
            result.append(p)
            result.append(n)
        return result

# Test cases
test_cases = [
    [3, 1, -2, -5, 2, -4],
    [-1, 1],
    [1, -1, 2, -2, 3, -3]
]

for i, nums in enumerate(test_cases, 1):
    print(f"Test Case {i}: {rearrangeArray(nums)}")

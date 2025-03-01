# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

def findMin(nums):
    start, end = 0, len(nums) - 1
    ans = float('inf')
    while start <= end:
        mid = start + (end - start) // 2
        if nums[start] <= nums[mid]:
            ans = min(ans, nums[start])
            start = mid + 1
        else:
            ans = min(ans, nums[mid])
            end = mid - 1
    return ans

# Example usage
if __name__ == "__main__":
    test_cases = [
        [3, 4, 5, 1, 2],
        [4, 5, 6, 7, 0, 1, 2],
        [11, 13, 15, 17],
        [2, 1]
    ]
    
    for i, nums in enumerate(test_cases, 1):
        result = findMin(nums)
        print(f"Test Case {i}: Minimum element is: {result}")
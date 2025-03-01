# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

def search(nums, target):
    start, end = 0, len(nums) - 1
    while start <= end:
        # Skip duplicates from the start
        while start < end and nums[start] == nums[start + 1]:
            start += 1
        
        # Skip duplicates from the end
        while start < end and nums[end] == nums[end - 1]:
            end -= 1
        
        mid = start + (end - start) // 2
        if nums[mid] == target:  # Target found
            return True
        if nums[start] <= nums[mid]:
            if nums[start] <= target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1    
        else:
            if nums[mid] < target <= nums[end]:
                start = mid + 1
            else:
                end = mid - 1
    return False

# Example usage
if __name__ == "__main__":
    test_cases = [
        ([2, 5, 6, 0, 0, 1, 2], 0),
        ([2, 5, 6, 0, 0, 1, 2], 3),
        ([1, 0, 1, 1, 1], 0),
        ([1, 1, 3, 1], 3)
    ]
    
    for i, (nums, target) in enumerate(test_cases, 1):
        result = search(nums, target)
        print(f"Test Case {i}: Target {target} found: {result}")
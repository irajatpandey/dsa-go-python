def search(nums, target):
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] == target:  # Target found
            return mid
        if nums[start] <= nums[mid]:
            if nums[start] <= target and target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1    
        else:
            if nums[mid] < target and target <= nums[end]:
                start = mid + 1
            else:
                end = mid - 1
    return -1

# Example usage
if __name__ == "__main__":
    test_cases = [
        ([4, 5, 6, 7, 0, 1, 2], 0),
        ([4, 5, 6, 7, 0, 1, 2], 3),
        ([1], 0),
        ([1, 3], 3)
    ]
    
    for i, (nums, target) in enumerate(test_cases, 1):
        result = search(nums, target)
        print(f"Test Case {i}: Target {target} found at index: {result}")
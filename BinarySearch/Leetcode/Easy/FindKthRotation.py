# https://www.geeksforgeeks.org/problems/rotation4723/1

def findKRotation(nums):
    start, end = 0, len(nums) - 1
    
    while start <= end:
        if nums[start] <= nums[end]:  # Already sorted (no rotation)
            return start
        
        mid = start + (end - start) // 2
        next_idx = (mid + 1) % len(nums)
        prev_idx = (mid - 1 + len(nums)) % len(nums)

        if nums[mid] <= nums[prev_idx] and nums[mid] <= nums[next_idx]:  
            return mid  # Index of the smallest element (number of rotations)
        
        if nums[start] <= nums[mid]:  # Left half is sorted, pivot is in right half
            start = mid + 1
        else:
            end = mid - 1
    
    return 0  # Edge case (not rotated)

# Example usage
if __name__ == "__main__":
    test_cases = [
        [15, 18, 2, 3, 6, 12],
        [7, 9, 11, 12, 5],
        [7, 9, 11, 12, 15],
        [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
    ]
    
    for i, nums in enumerate(test_cases, 1):
        result = findKRotation(nums)
        print(f"Test Case {i}: Array is rotated {result} times")
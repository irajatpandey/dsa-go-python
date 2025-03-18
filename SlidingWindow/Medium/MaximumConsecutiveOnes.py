
#Better
#Time Complexity : O(N) + O(N)
def longestOnes(self, nums, k):
    left, right, max_len = 0, 0, 0
    zeroCount = 0
    while right < len(nums):
        if nums[right] == 0:
            zeroCount += 1
        while zeroCount > k:
            if nums[left] == 0:
                zeroCount -= 1
            left += 1
        max_len = max(max_len, right - left + 1)
        right += 1          
    return max_len


# Optimal
""" 
Sliding Window Approach: Expands the window with right, shrinks it with left when zeroCount > k.
Tracks Zeroes: Uses zeroCount to count 0s in the window.
Adjusts Window: If zeroCount > k, moves left until the condition is met.
Max Subarray Length: Updates max_len at each step.
Time Complexity: O(N), each element processed at most twice.

"""
def longestOnes(self, nums, k):
    left, right, max_len = 0, 0, 0
    zeroCount = 0
    
    while right < len(nums):
        if nums[right] == 0:
            zeroCount += 1
        if zeroCount > k:
            if nums[left] == 0:
                zeroCount -= 1
            left += 1
        max_len = max(max_len, right - left + 1)
        right += 1
    return max_len
    
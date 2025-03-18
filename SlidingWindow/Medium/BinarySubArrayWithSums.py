def atMost(self, nums, goal):
    if goal < 0:
        return 0
    left, right, ans, total = 0, 0, 0, 0
    while right < len(nums):
        total += nums[right]
        while left <= right and total > goal:
            total -= nums[left]
            left += 1
        ans += right - left + 1
        right += 1
    return ans
def numSubarraysWithSum(self, nums, goal):
    return self.atMost(nums, goal) - self.atMost(nums, goal - 1)
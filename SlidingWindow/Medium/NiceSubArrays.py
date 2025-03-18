def atMost(self, nums, k):
    left, right, ans, count = 0, 0, 0, 0
    while right < len(nums):
        if nums[right] % 2 != 0:
            count += 1
        while left <= right and count > k:
            if nums[left] % 2 != 0:
                count -= 1
            left += 1
        ans += right - left + 1
        right += 1
    return ans
def numberOfSubarrays(self, nums, k):
    return self.atMost(nums, k) - self.atMost(nums, k - 1)
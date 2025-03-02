#https://leetcode.com/problems/single-element-in-a-sorted-array/
class Solution(object):
    def singleNonDuplicate(self, nums):
        start, end, ans = 0, len(nums) - 1, -1
        while start < end:
            mid = start + (end - start) // 2
            if mid % 2 == 0:
                if nums[mid] == nums[mid + 1]:
                    start = mid + 2
                else:
                    end = mid
            else:
                if nums[mid] == nums[mid - 1]:
                    start = mid + 1
                else:
                    end = mid
        return nums[start]

         
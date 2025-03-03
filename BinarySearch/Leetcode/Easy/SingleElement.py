def singleNonDuplicate(self, nums):
        n = len(nums)
        if len(nums) == 1:
            return nums[0]
        if nums[0] != nums[1]:
             return nums[0]

        if nums[n - 1] != nums[n - 2]:
            return nums[n - 1]
        
        start, end = 0, n - 2
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] != nums[mid + 1] and nums[mid] != nums[mid - 1]:
                return nums[mid]
            
            if mid % 2 == 1 and nums[mid - 1] == nums[mid] or mid % 2 == 0 and nums[mid] == nums[mid + 1]:
                start = mid + 1
            else:
                end = mid - 1
        
        return -1
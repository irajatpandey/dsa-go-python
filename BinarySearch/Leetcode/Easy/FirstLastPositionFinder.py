#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
class Solution(object):
    def firstOccurrence(self, nums, target):
        answer = -1
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
               answer = mid
               end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return answer
    
    def lastOccurrence(self, nums, target):
        start = 0
        end = len(nums) - 1
        answer = -1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
               answer = mid
               start = mid + 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return answer

    def searchRange(self, nums, target):
        return [self.firstOccurrence(nums, target), self.lastOccurrence(nums, target)]

# Driver code

def main():
    obj = Solution()
    
    test_cases = [
        ([5, 7, 7, 8, 8, 10], 8),  # Expected output: [3, 4]
        ([5, 7, 7, 8, 8, 10], 6),  # Expected output: [-1, -1]
        ([], 0),                   # Expected output: [-1, -1]
        ([1], 1),                  # Expected output: [0, 0]
        ([1, 1, 1, 1, 1], 1)       # Expected output: [0, 4]
    ]
    
    for nums, target in test_cases:
        print(f"Array: {nums}, Target: {target} -> First and Last Occurrence: {obj.searchRange(nums, target)}")
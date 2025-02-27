class Solution:
    def searchInsert(self, nums, target):
        start = 0
        end = len(nums) - 1
        answer = len(nums)

        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] >= target:
                answer = mid
                end = mid - 1
            else:
                start = mid + 1
        return answer

# Driver function with static test cases
def main():
    ob = Solution()
    
    test_cases = [
        ([1, 3, 5, 6], 5),  # Expected output: 2
        ([1, 3, 5, 6], 2),  # Expected output: 1
        ([1, 3, 5, 6], 7),  # Expected output: 4
        ([1, 3, 5, 6], 0),  # Expected output: 0
        ([1], 0),           # Expected output: 0
        ([1], 2)            # Expected output: 1
    ]
    
    for nums, target in test_cases:
        print(f"Array: {nums}, Target: {target} -> Insert Position: {ob.searchInsert(nums, target)}")

if __name__ == "__main__":
    main()

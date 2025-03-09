class Solution:
    def isPossible(self, stalls, k, mid):
        cows = 1
        last = stalls[0]
        for i in range(1, len(stalls)):
            if stalls[i] - last >= mid:
                cows += 1
                last = stalls[i]
            if cows >= k:
                return True
        return False

    def aggressiveCows(self, stalls, k):
        stalls.sort()  # Sort the stalls
        start = 0
        end = stalls[-1] - stalls[0]
        
        while start <= end:
            mid = start + (end - start) // 2
            if self.isPossible(stalls, k, mid):
                start = mid + 1
            else:
                end = mid - 1
        return end

# Example usage
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([1, 2, 4, 8, 9], 3),
        ([10, 1, 2, 7, 5], 4),
        ([4, 2, 1, 3, 6], 2)
    ]
    
    for i, (stalls, k) in enumerate(test_cases, 1):
        result = solution.aggressiveCows(stalls, k)
        print(f"Test Case {i}: Maximum minimum distance is: {result}")
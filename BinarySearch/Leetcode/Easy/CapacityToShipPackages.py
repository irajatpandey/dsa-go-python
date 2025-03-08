#https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/
class Solution(object):
    def canShip(self, weights, days, mid):
        total_weight, count = 0, 1  # Count ko 1 se start karo
        for weight in weights:
            total_weight += weight
            if total_weight > mid:
                count += 1
                total_weight = weight  # Reset sum to current weight, not 0
        return count <= days

    def shipWithinDays(self, weights, days):
        start, end = max(weights), sum(weights)  # start = max(weights) hona chahiye
        while start <= end:
            mid = start + (end - start) // 2
            if self.canShip(weights, days, mid):
                end = mid - 1
            else:
                start = mid + 1
        return start

# Example usage
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5),
        ([3, 2, 2, 4, 1, 4], 3),
        ([1, 2, 3, 1, 1], 4)
    ]
    
    for i, (weights, days) in enumerate(test_cases, 1):
        result = solution.shipWithinDays(weights, days)
        print(f"Test Case {i}: Minimum capacity to ship within {days} days is: {result}")
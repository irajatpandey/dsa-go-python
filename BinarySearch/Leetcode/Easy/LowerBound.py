class Solution:
    def findFloor(self, arr, k):
        start = 0
        end = len(arr) - 1  # Fix: Correcting the boundary
        answer = -1  # Default case if no floor exists

        while start <= end:
            mid = start + (end - start) // 2
            if arr[mid] <= k:
                answer = mid  # Update answer since this is a potential floor
                start = mid + 1  # Move right to find a closer floor value
            else:
                end = mid - 1  # Move left if arr[mid] > k

        return answer

# Driver Code
if __name__ == "__main__":
    t = int(input("Enter number of test cases: "))
    for _ in range(t):
        arr = list(map(int, input("Enter sorted array: ").split()))
        k = int(input("Enter value of k: "))
        obj = Solution()
        result = obj.findFloor(arr, k)
        print(f"Floor index of {k}: {result}")

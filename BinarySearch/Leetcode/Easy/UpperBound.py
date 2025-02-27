class Solution:
    def findFloor(self, arr, k):
        start = 0
        end = len(arr) - 1
        answer = -1  

        while start <= end:
            mid = start + (end - start) // 2
            if arr[mid] <= k:
                answer = mid  
                start = mid + 1  
            else:
                end = mid - 1  

        return arr[answer] if answer != -1 else -1  

    def findCeil(self, arr, k):
        start = 0
        end = len(arr) - 1
        answer = -1  

        while start <= end:
            mid = start + (end - start) // 2
            if arr[mid] >= k:
                answer = mid  
                end = mid - 1  
            else:
                start = mid + 1  

        return arr[answer] if answer != -1 else -1  

    def getFloorAndCeil(self, x: int, arr: list) -> list:
        arr.sort()  # Important: Binary search needs sorted array
        return [self.findFloor(arr, x), self.findCeil(arr, x)]

# Driver Code
def main():
    t = int(input())
    for _ in range(t):
        x = int(input())
        arr = list(map(int, input().split()))

        ob = Solution()
        ans = ob.getFloorAndCeil(x, arr)
        print(ans[0], ans[1])

if __name__ == "__main__":
    main()

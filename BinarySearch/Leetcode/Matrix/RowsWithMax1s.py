#https://www.geeksforgeeks.org/problems/row-with-max-1s0023/1
class Solution:
    def lower_bound(self, row):
        """Returns the index of the first occurrence of 1 in a sorted row"""
        start, end = 0, len(row) - 1
        ans = len(row)  # Default index if no 1 is found
        while start <= end:
            mid = start + (end - start) // 2
            if row[mid] == 1:
                ans = mid
                end = mid - 1  # Move left
            else:
                start = mid + 1  # Move right
        return ans  # If no 1 is found, ans will be len(row) 

    def rowWithMax1s(self, arr):
        """Finds the row index with the maximum number of 1s"""
        ans = -1
        maxCount = 0
        for i in range(len(arr)):
            firstIndex = self.lower_bound(arr[i])
            countOnes = len(arr[i]) - firstIndex  # Total 1s in this row
            
            if countOnes > maxCount:
                maxCount = countOnes
                ans = i  # Store the row index
        
        return ans

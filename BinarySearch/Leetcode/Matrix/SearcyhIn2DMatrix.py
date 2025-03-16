#https://leetcode.com/problems/search-a-2d-matrix/

""" 
Given a mid index in the flattened array:

Row index: row = mid // n
Since each row contains n elements, dividing by n gives the row number.
Column index: col = mid % n
Since columns repeat every n elements, taking modulo n gives the column number.


"""
# Time Complexity : O(log(m * n))
def searchMatrix(self, matrix, target):
    m, n = len(matrix), len(matrix[0])  # ✅ Rows and columns
    start, end = 0, (m * n) - 1
    while start <= end:
        mid = start + (end - start) // 2
        row = mid // n
        col = mid % n

        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False
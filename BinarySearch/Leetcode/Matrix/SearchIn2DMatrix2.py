#https://leetcode.com/problems/search-a-2d-matrix-ii/
class Solution:
    def searchMatrix(self, matrix, target):
        """
        Searches for the target value in a 2D matrix where:
        - Each row is sorted in ascending order.
        - Each column is sorted in ascending order.

        Approach:
        - Start from the top-right corner.
        - Move left if the current value is greater than the target.
        - Move down if the current value is smaller than the target.

        Time Complexity: O(m + n), where m = number of rows, n = number of columns.
        Space Complexity: O(1)

        :param matrix: List[List[int]], the 2D sorted matrix
        :param target: int, the value to search for
        :return: bool, True if target is found, otherwise False
        """
        if not matrix or not matrix[0]:  
            return False  # Handle empty matrix case

        m, n = len(matrix), len(matrix[0])  # Get matrix dimensions
        row, col = 0, n - 1  # Start from the top-right corner

        # Traverse the matrix
        while row < m and col >= 0:
            if matrix[row][col] == target:  # Target found
                return True
            elif matrix[row][col] < target:  # Move down
                row += 1
            else:  # Move left
                col -= 1
        
        return False  # Target not found

# Driver code
if __name__ == "__main__":
    # Example test cases
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    target = 5

    solution = Solution()
    print(solution.searchMatrix(matrix, target))  # Output: True

    target = 20
    print(solution.searchMatrix(matrix, target))  # Output: False

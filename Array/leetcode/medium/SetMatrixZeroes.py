# https://leetcode.com/problems/set-matrix-zeroes/description/

def set_zeroes(matrix):
    row_len = len(matrix)
    col_len = len(matrix[0])

    coordinates = []
    for i in range(row_len):
        for j in range(col_len):
            coordinate = []
            if matrix[i][j] == 0:
                coordinate.append(i)
                coordinate.append(j)
                coordinates.append(coordinate)     
    for pair in coordinates:
        x = pair[0]
        y = pair[1]
        for j in range(col_len):
            matrix[x][j] = 0
        for i in range(row_len):
            matrix[i][y] = 0 
    

# Example usage
if __name__ == "__main__":
    matrix = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    set_zeroes(matrix)
    print("Matrix after setting zeroes:")
    for row in matrix:
        print(row)
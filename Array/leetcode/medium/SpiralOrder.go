// https://leetcode.com/problems/spiral-matrix/
package main

import "fmt"

func spiralOrder(matrix [][]int) []int {
    if len(matrix) == 0 {
        return []int{}
    }

    result := []int{}
    top, bottom := 0, len(matrix)-1
    left, right := 0, len(matrix[0])-1

    for top <= bottom && left <= right {
        // Traverse from left to right
        for i := left; i <= right; i++ {
            result = append(result, matrix[top][i])
        }
        top++

        // Traverse from top to bottom
        for i := top; i <= bottom; i++ {
            result = append(result, matrix[i][right])
        }
        right--

        if top <= bottom {
            // Traverse from right to left
            for i := right; i >= left; i-- {
                result = append(result, matrix[bottom][i])
            }
            bottom--
        }

        if left <= right {
            // Traverse from bottom to top
            for i := bottom; i >= top; i-- {
                result = append(result, matrix[i][left])
            }
            left++
        }
    }

    return result
}

func spiralOrderHelper() {
    matrix := [][]int{
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9},
    }
    result := spiralOrder(matrix)
    fmt.Println("Spiral order of the matrix is:", result)
}
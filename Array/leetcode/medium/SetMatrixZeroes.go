// https://leetcode.com/problems/set-matrix-zeroes/

package main

import "fmt"

func setZeroes(matrix [][]int) {
    row_len, col_len  := len(matrix), len(matrix[0])
    coordinates := make([][]int, 0)
    for i := 0; i < row_len; i++ {
        for j := 0; j < col_len; j++ {
            coordinate := make([]int, 0)
            if matrix[i][j] == 0 {
               coordinate = append(coordinate, i)
               coordinate = append(coordinate, j)
               coordinates = append(coordinates, coordinate)
            }
        }
    }

    for _, item := range coordinates {
        x := item[0]
        y := item[1]

        for j := 0; j < col_len; j++ {
            matrix[x][j] = 0
        }
        for i := 0; i < row_len; i++ {
            matrix[i][y] = 0
        }
    }
    
}

func setZeroesHelper() {
    matrix := [][]int{
        {1, 1, 1},
        {1, 0, 1},
        {1, 1, 1},
    }
    setZeroes(matrix)
    fmt.Println("Matrix after setting zeroes:")
    for _, row := range matrix {
        fmt.Println(row)
    }
}
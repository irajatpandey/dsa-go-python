// https://leetcode.com/problems/rearrange-array-elements-by-sign/description/
package main

import "fmt"

func rearrangeArray(nums []int) []int {
     positive := make([]int, 0)
     negative := make([]int, 0)
     result := make([]int, 0)

     for _, num := range nums {
        if num < 0 {   
            negative = append(negative, num)
        } else {
            positive = append(positive, num)
        }
     }

    for i := 0; i < len(positive) || i < len(negative); i++ {
        if i < len(positive) {
            result = append(result, positive[i])
        }
        if i < len(negative) {
            result = append(result, negative[i])
        }
    }

    return result
}

func rearrangeArrayHelper() {
    testCases := [][]int{
        {3, 1, -2, -5, 2, -4},
        {-1, 1},
        {1, -1, 2, -2, 3, -3},
    }

    for i, nums := range testCases {
        fmt.Printf("Test Case %d: %v\n", i+1, rearrangeArray(nums))
    }
    fmt.Println()
}

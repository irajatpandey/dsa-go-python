// https://leetcode.com/problems/maximum-subarray/description/
package main

import (
	"fmt"
	"math"
)
func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func maxSubArray(nums []int) int {
	maxSum, currentSum := math.MinInt32, 0
    for _, value := range nums {
       if currentSum + value > value {
        currentSum += value
       } else {
        currentSum = value
       }
       maxSum = max(currentSum, maxSum) 
    }
   
   return maxSum
}

func maxSubArrayHelper() {
    testCases := [][]int{
        {-2, 1, -3, 4, -1, 2, 1, -5, 4},
        {1},
        {5, 4, -1, 7, 8},
        {-1, -2, -3, -4},
    }

    for i, testCase := range testCases {
        result := maxSubArray(testCase)
        fmt.Printf("Test Case %d: %d\n", i+1, result)
    }
}

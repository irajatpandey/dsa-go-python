// https://leetcode.com/problems/next-permutation/description/
package main

import "fmt"

func nextPermutation(nums []int) {
   
}

func nextPermutationHelper() {
    testCases := [][]int{
        {1, 2, 3},
        {3, 2, 1},
        {1, 1, 5},
        {1, 3, 2},
    }

    for i, nums := range testCases {
        fmt.Printf("Test Case %d: Before: %v, ", i+1, nums)
        nextPermutation(nums)
        fmt.Printf("After: %v\n", nums)
    }
    fmt.Println()
}
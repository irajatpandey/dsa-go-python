// https://leetcode.com/problems/sort-colors/
package main

import "fmt"

func sortColors(nums []int) {
	i, j, k := 0, 0, len(nums) - 1
	for j <= k  {
	   if nums[j] == 2 {
		   nums[j], nums[k] = nums[k], nums[j]
		   k--;
	   } else if nums[j] == 1 {
		   j++
	   } else {
		   nums[i], nums[j] = nums[j], nums[i]
		   i++   
		   j++
	   }
	}
}

func sortColorsMain() {
    testCases := [][]int{
        {2, 0, 2, 1, 1, 0},
        {2, 0, 1},
        {0},
        {1},
    }

    for i, testCase := range testCases {
        sortColors(testCase)
        fmt.Printf("Test Case %d: %v\n", i+1, testCase)
    }
}


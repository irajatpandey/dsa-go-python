// https://leetcode.com/problems/majority-element/description/
package main

import "fmt"

func majorityElement(nums []int) int {
     count := 0
	 candidate := 0

	 for _, value := range(nums) {
		 if count == 0 {
			 candidate = value
		 }
		 if value == candidate {
			 count++
		 } else {
			 count--
		 }
	 }
	 return candidate
}

func majorityElementHelper() {
    testCases := [][]int{
        {3, 2, 3},
        {2, 2, 1, 1, 1, 2, 2},
        {1},
        {6, 5, 5},
    }

    for i, testCase := range testCases {
        result := majorityElement(testCase)
        fmt.Printf("Test Case %d: %d\n", i+1, result)
    }
}

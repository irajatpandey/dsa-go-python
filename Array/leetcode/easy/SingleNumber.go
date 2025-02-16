// https://leetcode.com/problems/single-number/
package main

import "fmt"

func singleNumber(nums []int, n int) int {
	result := 0

	for _, value := range(nums) {
	   result ^= value
	}

	return result
}

func singleNumberMain() {
    arr1 := []int{1, 2, 1, 2, 4}
    fmt.Println("Test Case 1:", singleNumber(arr1, len(arr1)))

    arr2 := []int{2, 2, 1}
    fmt.Println("Test Case 2:", singleNumber(arr2, len(arr2)))

    arr3 := []int{4, 1, 2, 1, 2}
    fmt.Println("Test Case 3:", singleNumber(arr3, len(arr3)))
}

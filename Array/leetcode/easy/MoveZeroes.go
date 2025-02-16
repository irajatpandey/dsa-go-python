// https://leetcode.com/problems/move-zeroes/description/
package main

import "fmt"

// Moves all zeros in the array to the end without changing the order of non-zero elements.
func moveZeroes(nums []int) {
	i := 0
    for j := 0; j < len(nums); j++ {
        if nums[j] != 0 {
            nums[i], nums[j] = nums[j], nums[i]
            i++
        }
    }
}

func moveZeroesMain() {
	// Test Case 1
	arr1 := []int{0, 1, 0, 3, 12}
	moveZeroes(arr1)
	fmt.Print("Test Case 1: ")
	for _, ele := range arr1 {
		fmt.Print(ele, " ")
	}
	fmt.Println() // Expected output: 1 3 12 0 0

	// Test Case 2
	arr2 := []int{0, 0, 0, 1, 0}
	moveZeroes(arr2)
	fmt.Print("Test Case 2: ")
	for _, ele := range arr2 {
		fmt.Print(ele, " ")
	}
	fmt.Println() // Expected output: 1 0 0 0 0

	// Test Case 3
	arr3 := []int{1, 2, 3, 4, 5}
	moveZeroes(arr3)
	fmt.Print("Test Case 3: ")
	for _, ele := range arr3 {
		fmt.Print(ele, " ")
	}
	fmt.Println() // Expected output: 1 2 3 4 5
}


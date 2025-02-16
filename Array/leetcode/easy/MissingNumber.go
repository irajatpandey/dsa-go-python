package main

import "fmt"

// missingNumber finds the missing number in an array of distinct integers from 0 to n.
func missingNumber(nums []int) int {
	n := len(nums)
    sum := 0
    total := (n * (n + 1) / 2)
    for _, value := range(nums){
        sum += value
    }
    
    return total - sum
}

func missing_number_main() {
    // Test Case 1
    arr1 := []int{0, 1, 3}
    fmt.Println("Test Case 1:", missingNumber(arr1)) // Expected: 2

    // Test Case 2
    arr2 := []int{0, 1, 2, 4, 5}
    fmt.Println("Test Case 2:", missingNumber(arr2)) // Expected: 3

    // Test Case 3
    arr3 := []int{9, 6, 4, 2, 3, 5, 7, 0, 1}
    fmt.Println("Test Case 3:", missingNumber(arr3)) // Expected: 8
}

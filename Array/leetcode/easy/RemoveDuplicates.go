// https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
package main

import "fmt"

func removeDuplicates(nums []int, n int) int {
	i := 0
    for j := 0; j < len(nums); j++ {
        if nums[i] != nums[j] {
            nums[i + 1] = nums[j]
            i++
        }
    }
    return i + 1
}

func removeDuplicatesMain() {
    arr1 := []int{1, 2, 2, 2, 3, 3, 4}
    output1 := removeDuplicates(arr1, len(arr1))
    fmt.Println("Test Case 1: New length =", output1)

    arr2 := []int{1, 1, 2, 2, 3, 3, 3}
    output2 := removeDuplicates(arr2, len(arr2))
    fmt.Println("Test Case 2: New length =", output2)

    arr3 := []int{1, 1, 1, 1, 1}
    output3 := removeDuplicates(arr3, len(arr3))
    fmt.Println("Test Case 3: New length =", output3)
}

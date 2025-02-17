package main

import "fmt"
func reverseInPlace(slice []int) {
    for i, j := 0, len(slice)-1; i < j; i, j = i+1, j-1 {
        // Swap elements
        slice[i], slice[j] = slice[j], slice[i]
    }
}

// findLeaders finds all leaders in the array.
// A leader is an element which is greater than all the elements to its right.
func findLeaders(nums []int) []int {
	 result := make([]int, 0)
     currentLeader := nums[len(nums) - 1]
	 result = append(result, currentLeader)
     for i := len(nums) - 2; i >= 0; i-- {
        if nums[i] >= currentLeader {
            currentLeader = nums[i]
            result = append(result, currentLeader)
        }
     }

     reverseInPlace(result)
     return result

}

func findLeadersHelper() {
    arr := []int{16, 17, 4, 3, 5, 2}
    leaders := findLeaders(arr)
    fmt.Printf("Leaders in the array are: %v\n", leaders)
}
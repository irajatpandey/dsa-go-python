package main

import "fmt"

// check verifies if the array can be sorted by a single rotation
func check(arr []int) bool {
    count := 0  // Count the number of "out of order" points

    for i := 0; i < len(arr); i++ {
        // If current element is greater than the next element (cyclically), increment count
        if arr[i] > arr[(i+1)%len(arr)] {
            count++
        }
    }

    // The array can be rotated to become sorted if there's at most one out-of-order point
    return count <= 1
}

// Driver function for testing
func checkMain() {
    arr := []int{3, 4, 5, 1, 2}
    fmt.Println("Is rotated sorted array:", check(arr)) // Expected Output: true
}

package main

import "fmt"

// reverseArray reverses the given array in place.
func reverseArray(arr []int) []int {
    
	start := 0
	end := len(arr) - 1

	for start < end {
		arr[start], arr[end] = arr[end], arr[start]
		start++
		end--
	}
    return arr
}

// Example usage
func reverseArrayMain() {
	arr := []int{1, 2, 3, 4, 5}
	fmt.Println("Original array:", arr)
	reversedArr := reverseArray(arr)
	fmt.Println("Reversed array:", reversedArr)
}
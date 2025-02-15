package main

import "fmt"

// insertionSort implements the Insertion Sort algorithm to sort an array in ascending order.
func insertionSort(arr []int) {
	for i := 1; i < len(arr); i++ {
		key := arr[i]  // Current element to be placed at the correct position
		j := i - 1

		// Shift elements to the right until the correct position for key is found
		for j >= 0 && arr[j] > key {
			arr[j+1] = arr[j]  // Move element one position ahead
			j--
		}

		arr[j+1] = key // Insert the key at the correct position
	}

	// Print the sorted array
	fmt.Print("Sorted array: ")
	for _, value := range arr {
		fmt.Print(value, " ")
	}
	fmt.Println()
}

// insertionSortMain serves as the driver function to test the sorting algorithm.
func insertionSortMain() {
	arr := []int{64, 34, 25, 12, 22, 11, 90}
	fmt.Println("Original array:", arr)
	insertionSort(arr)
}

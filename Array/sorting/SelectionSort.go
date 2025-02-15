package main

import "fmt"

// selectionSort implements Selection Sort algorithm
func selectionSort(arr []int) {
    n := len(arr)
    
    for i := 0; i < n-1; i++ {
        minIndex := i
        
        // Find the minimum element in the remaining unsorted part
        for j := i + 1; j < n; j++ {
            if arr[j] < arr[minIndex] {
                minIndex = j
            }
        }
        
        // Swap the found minimum element with the first unsorted element
        arr[minIndex], arr[i] = arr[i], arr[minIndex]
    }

    // Print the sorted array
    fmt.Print("Sorted array: ", arr)
    
}

// Driver function to test the sorting algorithm
func selectionSortMain() {
    arr := []int{64, 34, 25, 12, 22, 11, 90}
    fmt.Println("Original array:", arr)
    selectionSort(arr)
}

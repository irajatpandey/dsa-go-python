package main

import "fmt"

func linearSearch(arr []int, target int) {
    for _, value := range(arr) {
        if value == target {
            fmt.Println("Element found in an array")
			return
        }
	}
    fmt.Println("Element not found")

}

func linearSearchMain() {
    arr := []int{1, 2, 3, 4, 5}
    target := 3
    linearSearch(arr, target)
}
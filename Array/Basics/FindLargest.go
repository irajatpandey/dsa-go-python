package main
import "fmt"

func getLargest (arr [5] int) int {
	max := arr[0]

	for _, value := range arr {
		if value > max {
			max = value
		}
	}
	return max
}
func findLargestMain() {
  arr := [5]int{12, 34, 56, 78, 90}

  largest := getLargest(arr)
  fmt.Println("Largest Element in the Array is: ", largest)
}
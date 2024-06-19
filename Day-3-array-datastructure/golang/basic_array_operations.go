package main

import "fmt"

func main() {
	// Creating an array
	arr := []int{1, 2, 3, 4, 5}

	// Accessing elements
	fmt.Println(arr[0]) // Output: 1
	fmt.Println(arr[2]) // Output: 3

	// Inserting an element (using slices)
	arr = append(arr[:2], append([]int{10}, arr[2:]...)...)
	fmt.Println(arr) // Output: [1, 2, 10, 3, 4, 5]

	// Deleting an element (using slices)
	arr = append(arr[:2], arr[3:]...)
	fmt.Println(arr) // Output: [1, 2, 3, 4, 5]

	// Searching for an element
	index := -1
	for i, v := range arr {
		if v == 3 {
			index = i
			break
		}
	}
	fmt.Println(index) // Output: 2

	// Updating an element
	arr[1] = 20
	fmt.Println(arr) // Output: [1, 20, 3, 4, 5]
}

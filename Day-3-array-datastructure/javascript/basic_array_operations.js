// Creating an array
let arr = [1, 2, 3, 4, 5];

// Accessing elements
console.log(arr[0]); // Output: 1
console.log(arr[2]); // Output: 3

// Inserting an element
arr.splice(2, 0, 10); // Inserts 10 at index 2
console.log(arr); // Output: [1, 2, 10, 3, 4, 5]

// Deleting an element
arr.splice(2, 1); // Removes element at index 2
console.log(arr); // Output: [1, 2, 3, 4, 5]

// Searching for an element
let index = arr.indexOf(3);
console.log(index); // Output: 2

// Updating an element
arr[1] = 20;
console.log(arr); // Output: [1, 20, 3, 4, 5]

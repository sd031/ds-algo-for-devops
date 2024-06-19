// Creating a 2D array
let arr2D = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];

// Accessing elements
console.log(arr2D[0][1]); // Output: 2
console.log(arr2D[2][2]); // Output: 9

// Traversing a 2D array
for (let row of arr2D) {
    for (let elem of row) {
        process.stdout.write(elem + ' ');
    }
}
// Output: 1 2 3 4 5 6 7 8 9
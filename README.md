# DSA PROJECT

This project provides Python implementations and solutions for the Bubble sorting method , Matrix chain multiplication using Dynamic Programming and N-Queens problem using a backtracking algorithm.

---The Bubble sorting method helps in sorting the array in easy manner.It is generally not recommended for large datasets due to its poor time complexity.
---The Dynamic programming algorithm provides an optimum solution for many problems such as matrix multiplication etc.,
---The N-Queens problem is about placing N chess queens on an N×N chessboard so that no two queens threaten each other.

## Problem Descriptions

### Question 1

You are given an array of integers, and you are required to sort this array using one of the following sorting algorithms: Bubble Sort, Selection Sort, or Insertion Sort. Your task is to implement the chosen sorting algorithm and analyze its time complexity.
1.	Implement one of the sorting algorithms mentioned above (Bubble Sort, Selection Sort, or Insertion Sort) in Python.
2.	Apply your sorting algorithm to the given array of integers.
3.	Provide the sorted array as the output.
4.	Analyze the time complexity of the sorting algorithm you implemented. Explain whether it is a stable sort and how it performs on different types of input data (e.g., already sorted, reverse sorted, random data).
5.	Compare the time complexity of your chosen sorting algorithm with at least one other sorting algorithm (e.g., Quick Sort, Merge Sort, or Python's built-in sorted function). Explain the differences and scenarios where one algorithm might be preferred over the other.
Input:
•	An unsorted list of integers (e.g., [5, 2, 9, 1, 5, 6]).
Output:
•	The sorted list of integers.
Instructions:
1.	Choose one of the sorting algorithms (Bubble Sort, Selection Sort, or Insertion Sort) and implement it in Python.
2.	Apply your chosen sorting algorithm to the provided input array.
3.	Provide the sorted array as the output.
4.	Analyze the time complexity of the sorting algorithm and discuss its stability and performance on different input data.
5.	Compare the time complexity of your chosen sorting algorithm with at least one other sorting algorithm, and explain when you would prefer one over the other.


### Question 2

You are given a sequence of matrices with dimensions that are suitable for matrix multiplication. Your task is to find the optimal way to parenthesize the matrices to minimize the total number of scalar multiplications required to compute their product.
1.	Implement a dynamic programming algorithm in Python to solve the matrix chain multiplication problem.
2.	Apply your algorithm to the given sequence of matrices and find the optimal parenthesization.
3.	Calculate and provide the minimum number of scalar multiplications required for the optimal parenthesization.
4.	Explain the dynamic programming approach you used, including the initialization, recurrence relation, and how you reconstructed the optimal parenthesization.
5.	Analyze the time and space complexity of your algorithm, and discuss its efficiency in solving large instances of the problem.
Input:
•	A list of matrices, each represented by its dimensions. For example, a list of matrices [A, B, C] could be represented as [(2, 3), (3, 4), (4, 2)] where the dimensions of matrix A are 2x3, the dimensions of matrix B are 3x4, and the dimensions of matrix C are 4x2.
Output:
•	The optimal parenthesization of matrices as a sequence of matrix multiplications.
•	The minimum number of scalar multiplications required for the optimal parenthesization.
Instructions:
1.	Implement a dynamic programming algorithm to solve the matrix chain multiplication problem in Python.
2.	Apply your algorithm to the provided list of matrices to find the optimal parenthesization.
3.	Calculate and provide the minimum number of scalar multiplications required for the optimal parenthesization.
4.	Explain the dynamic programming approach, including the initialization, recurrence relation, and reconstruction of the optimal parenthesization.
5.	Analyze the time and space complexity of your algorithm and discuss its efficiency for large instances of the problem.

### Question 3

You are tasked with solving the N-Queens problem using a backtracking algorithm. The N-Queens problem is to place N chess queens on an N×N chessboard so that no two queens threaten each other. Thus, a solution requires that no two queens share the same row, column, or diagonal. Your goal is to implement the algorithm, find all possible solutions for a given N, and analyze its time complexity.
1.	Implement a backtracking algorithm in Python to solve the N-Queens problem.
2.	Apply your algorithm to find all possible solutions for a given N (e.g., N = 4 or N = 8). Ensure that you generate all unique solutions.
3.	Present the solutions as chessboard representations, indicating the placement of queens (e.g., using 'Q' for queens and '.' for empty squares).
4.	Explain the backtracking approach, including how you generate and validate solutions and how you handle conflicts between queens.
5.	Analyze the time complexity of your algorithm and discuss its efficiency for larger values of N.
Input:
•	An integer N (N ≥ 4) representing the size of the N×N chessboard and the number of queens to place.
Output:
•	All possible solutions to the N-Queens problem for the given N, presented as chessboard representations.
Instructions:
1.	Implement a backtracking algorithm to solve the N-Queens problem in Python.
2.	Apply your algorithm to find all possible solutions for the provided value of N (e.g., N = 4 or N = 8).
3.	Present the solutions as chessboard representations, indicating the placement of queens (e.g., using 'Q' for queens and '.' for empty squares).
4.	Explain the backtracking approach, including solution generation, validation, and conflict resolution.
5.	Analyze the time complexity of your algorithm and discuss its performance for larger N values.

## How to Use

- Clone this repository to your local machine.
- Run the Python scripts for each question to see the solutions and performance.

## Example

For example, to solve the N-Queens problem for N=4 using the backtracking algorithm, you can run `python question3.py`.



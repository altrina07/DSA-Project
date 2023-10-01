def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        # Flag to optimize the algorithm
        swapped = False
        
        for j in range(0, n-i-1):
            # If the current element is greater than the next element, swap them
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        # If no two elements were swapped in inner loop, the array is already sorted
        if not swapped:
            break

# Example input
input_array = [5, 2, 9, 1, 5, 6]

# Apply Bubble Sort
bubble_sort(input_array)

# Sorted array
print(input_array)

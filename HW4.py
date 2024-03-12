def selection_sort(arr):
    # Calculate the length of the array
    n = len(arr)
    
    # Iterate over each index in the array
    for i in range(n):
        # Assume the current index is the minimum
        min_idx = i
        
        # Iterate over the array
        for j in range(i+1, n):
            # Check if the current element is smaller than the minimum element
            if arr[j] < arr[min_idx]:
                # Update the minimum index if a smaller element is found
                min_idx = j
        
        # Swap the current element with the minimum element found
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# trying:
arr = [76, 22, 14, 20, 9]
# Sort the array using the function
selection_sort(arr)
# Print the sorted array
print("Sorted array:", arr)
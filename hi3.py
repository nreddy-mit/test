def bubble_sort(arr):
    """
    Bubble Sort - a simple sorting algorithm that repeatedly steps through the list,
    compares adjacent elements and swaps them if they are in the wrong order.
    """
    n = len(arr)
    # Create a copy to avoid modifying the original array
    arr_copy = arr.copy()
    
    # Traverse through all array elements
    for i in range(n):
        # Flag to optimize - if no swaps occur, array is sorted
        swapped = False
        
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            print(arr_copy[j], arr_copy[j + 1])

            if arr_copy[j] > arr_copy[j + 1]:
                # Swap if they are in wrong order
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                swapped = True
        
        # If no swapping occurred, array is sorted
        if not swapped:
            break
    
    return arr_copy

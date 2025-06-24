def bogo_sort(arr):
    """
    BOGO sort (Bogosort) - a highly inefficient sorting algorithm
    that randomly shuffles the array until it's sorted.
    """
    import random
    
    def is_sorted(arr):
        """Check if array is sorted in ascending order"""
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True
print(bogo_sort([3, 2, 1]))
print(bogo_sort([1, 2, 3]))
    # Keep shuffling until the array is sorted
    while not is_sorted(arr):
        random.shuffle(arr)
    
    return arr

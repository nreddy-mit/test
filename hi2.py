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
    
    # Keep shuffling until the array is sorted
    while not is_sorted(arr):
        random.shuffle(arr)
    
    return arr

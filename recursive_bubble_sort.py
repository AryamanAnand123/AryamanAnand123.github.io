def recursive_bubble_sort(arr, n=None):
    if n is None:
        n = len(arr)
    
    if n == 1:
        return arr
    
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
    return recursive_bubble_sort(arr, n - 1)

# Example usage
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = recursive_bubble_sort(arr)
    print("Sorted array:", sorted_arr)
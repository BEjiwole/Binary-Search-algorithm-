def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  

sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]
target_value = 9
index = binary_search(sorted_list, target_value)
if index != -1:
    print(f"Element {target_value} found at index {index}.")
else:
    print(f"Element {target_value} not found.")

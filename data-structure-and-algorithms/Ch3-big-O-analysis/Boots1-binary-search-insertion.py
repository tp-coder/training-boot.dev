# Find the insertion point for a target value in a sorted list using binary search.

def binary_search_insertion(target, arr):
    start = 0
    end = len(arr)

    while start < end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return f"Target {target} is already in the list at index {mid}"
        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid
    
    arr.insert(start, target)
    return f"Target {target} should be inserted at index {start}. The new list is {arr}"
        
# test cases
arr = [1, 3, 5, 7]
print(binary_search_insertion(0, arr))  # Should return 0
print(binary_search_insertion(4, arr))  # Should return 3
print(binary_search_insertion(4, arr))  # Target 4 is already in the list at index 2
print(binary_search_insertion(9, arr))  # Should return 6
print(binary_search_insertion(9, arr))  # Target 9 is already in the list at index 4
print(binary_search_insertion(8, arr))  # Should return 6
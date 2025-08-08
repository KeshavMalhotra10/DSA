# below is an example of binary search

# 1: find middle element of the list
# 2: if middle element is equal to target, return index of middle element
# 3: if middle element is less than target, search in right half of list
# 4: if middle element is greater than target, search in left half of list
# 5: repeat steps 1 to 4 until target is found or search interval is empty


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_number = arr[mid]

        print("left", left, "right", right, "mid", mid, "mid_number", mid_number)

        if mid_number == target:
            return mid
        elif mid_number < target:
            left = mid - 1
        elif mid_number > target:
            right = mid + 1
    return -1


# Example usage
binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)

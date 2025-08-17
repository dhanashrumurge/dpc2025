def findDuplicate(arr):
    # Step 1: Detect cycle
    slow = arr[0]
    fast = arr[0]

    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break

    # Step 2: Find the entrance to the cycle (duplicate number)
    finder = arr[0]
    while finder != slow:
        finder = arr[finder]
        slow = arr[slow]

    return finder
# Test cases
print(findDuplicate([1, 3, 4, 2, 2]))       # Output: 2
print(findDuplicate([3, 1, 3, 4, 2]))       # Output: 3
print(findDuplicate([1, 1]))                # Output: 1
print(findDuplicate([1, 4, 4, 2, 3]))       # Output: 4
print(findDuplicate([i for i in range(1, 100000)] + [50000]))  # Output: 50000

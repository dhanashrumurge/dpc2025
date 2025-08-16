def findMissingNumber(arr):
    n = len(arr) + 1   # one number is missing
    total_sum = n * (n + 1) // 2
    arr_sum = sum(arr)
    return total_sum - arr_sum

# ---- Test Cases ----
print(findMissingNumber([1, 2, 4, 5]))              # Output: 3
print(findMissingNumber([2, 3, 4, 5]))              # Output: 1
print(findMissingNumber([1, 2, 3, 4]))              # Output: 5
print(findMissingNumber([1]))                       # Output: 2
print(findMissingNumber(list(range(1, 1000000))))   # Output: 1000000

from collections import defaultdict

def find_zero_sum_subarrays(arr):
    """
    Find all subarrays of arr whose sum is zero.
    Returns a list of (start_index, end_index) tuples.
    """
    res = []
    prefix_sum = 0
    seen = defaultdict(list)

    # Prefix sum 0 is seen before starting the array at index -1
    seen[0].append(-1)

    for i, num in enumerate(arr):
        prefix_sum += num

        # If prefix_sum already seen, we found subarrays ending at i
        if prefix_sum in seen:
            for j in seen[prefix_sum]:
                res.append((j + 1, i))

        # Store index for this prefix sum
        seen[prefix_sum].append(i)

    return res


# -------------------------
# Test cases from the image
# -------------------------

print("Example:")
print(find_zero_sum_subarrays([1, 2, -3, -1, 2]))  # Expected [(0, 2), (1, 4)]

print("\nTest Case 1:")
print(find_zero_sum_subarrays([4, -1, -3, 1, 2, -1]))  # Expected [(1, 2), (0, 3)]

print("\nTest Case 2:")
print(find_zero_sum_subarrays([1, 2, 3, 4]))  # Expected []

print("\nTest Case 3:")
print(find_zero_sum_subarrays([0, 0, 0]))
# Expected [(0,0),(0,1),(1,1),(0,2),(1,2),(2,2)]

print("\nTest Case 4:")
print(find_zero_sum_subarrays([-3, 1, 2, -3, 4, 0]))
# Expected [(0,3),(4,4)]

print("\nTest Case 5: Large Input (showing only first 10 results)")
arr = [1, -1, 2, -2, 3, -3] * 10000  # size 60000
res = find_zero_sum_subarrays(arr)
print("Total zero-sum subarrays:", len(res))
print("First 10:", res[:10])
print("Last 5:", res[-5:])

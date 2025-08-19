def find_leaders(arr):
    leaders_rev = []
    max_so_far = float("-inf")

    # Traverse from right to left
    for x in reversed(arr):
        if x > max_so_far:
            leaders_rev.append(x)
            max_so_far = x

    # Reverse to maintain original order of appearance
    return leaders_rev[::-1]


# ----- Test Cases from the prompt -----
print(find_leaders([16, 17, 4, 3, 5, 2]))             # -> [17, 5, 2]

print(find_leaders([1, 2, 3, 4, 0]))                  # -> [4, 0]
print(find_leaders([7, 10, 4, 10, 6, 5, 2]))          # -> [10, 6, 5, 2]
print(find_leaders([5]))                              # -> [5]
print(find_leaders([100, 50, 20, 10]))                # -> [100, 50, 20, 10]
print(find_leaders(list(range(1, 1_000_000 + 1))))    # -> [1000000]

# ----- Edge Cases noted -----
# 1) Single element -> always a leader
print(find_leaders([42]))                             # -> [42]
# 2) Strictly descending -> every element is a leader
print(find_leaders([9, 7, 5, 3, 1]))                  # -> [9, 7, 5, 3, 1]
# 3) Strictly ascending -> only last is a leader
print(find_leaders([1, 2, 3, 4, 5]))                  # -> [5]

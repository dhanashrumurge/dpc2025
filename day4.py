import math

# Function to merge two sorted arrays in place using Gap method
def merge_in_place(arr1, arr2):
    m, n = len(arr1), len(arr2)

    def next_gap(gap):
        if gap <= 1:
            return 0
        return (gap // 2) + (gap % 2)

    gap = next_gap(m + n)
    while gap > 0:
        i = 0
        j = i + gap
        while j < (m + n):
            # Left element
            if i < m:
                a_i, A, Ai = arr1[i], arr1, i
            else:
                a_i, A, Ai = arr2[i - m], arr2, i - m

            # Right element
            if j < m:
                a_j, B, Bj = arr1[j], arr1, j
            else:
                a_j, B, Bj = arr2[j - m], arr2, j - m

            # Swap if needed
            if a_i > a_j:
                A[Ai], B[Bj] = B[Bj], A[Ai]

            i += 1
            j += 1

        gap = next_gap(gap)

# Test cases 
tests = [
    # Example from sheet
    ([1, 3, 5, 7], [2, 4, 6, 8]),

    # Test Case 1
    ([1, 3, 5], [2, 4, 6]),

    # Test Case 2
    ([10, 12, 14], [1, 3, 5]),

    # Test Case 3
    ([2, 3, 8], [4, 6, 10]),

    # Test Case 4
    ([1], [2]),

    # Test Case 5  
    (list(range(1, 1000001)), list(range( 50000, 1000001))) 



    
]

# Run and print results
for idx, (a1, a2) in enumerate(tests, 1):
    merge_in_place(a1, a2)
    print(f"Test Case {idx}:")
    print("  arr1 =", a1)
    print("  arr2 =", a2)
    print("-" * 40)

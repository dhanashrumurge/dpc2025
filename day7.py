def trap_rain_water(height):
    n = len(height)
    if n < 3:  # less than 3 bars cannot trap water
        return 0

    # Arrays to store max heights to the left and right
    max_left = [0] * n
    max_right = [0] * n

    # Fill max_left
    max_left[0] = height[0]
    for i in range(1, n):
        max_left[i] = max(max_left[i-1], height[i])

    # Fill max_right
    max_right[n-1] = height[n-1]
    for i in range(n-2, -1, -1):
        max_right[i] = max(max_right[i+1], height[i])

    # Calculate water trapped
    total_water = 0
    for i in range(n):
        total_water += max(0, min(max_left[i], max_right[i]) - height[i])

    return total_water

# Test cases
print(trap_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # Output: 6
print(trap_rain_water([4, 2, 0, 3, 2, 5]))                   # Output: 9
print(trap_rain_water([1, 1, 1]))                            # Output: 0
print(trap_rain_water([5]))                                  # Output: 0
print(trap_rain_water([2, 0, 2]))                            # Output: 2

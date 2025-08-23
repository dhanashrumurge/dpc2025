def longestCommonPrefix(strs):
    if not strs:  # Empty array
        return ""

    # Start with the first string as prefix
    prefix = strs[0]

    # Compare with each string
    for s in strs[1:]:
        # Reduce prefix until it matches the start of s
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix


# -------------------------------
# Test Cases
print(longestCommonPrefix(["flower", "flow", "flight"]))   # "fl"
print(longestCommonPrefix(["dog", "racecar", "car"]))      # ""
print(longestCommonPrefix(["apple", "ape", "april"]))      # "ap"
print(longestCommonPrefix([""]))                           # ""
print(longestCommonPrefix(["alone"]))                      # "alone"
print(longestCommonPrefix([]))                             # ""

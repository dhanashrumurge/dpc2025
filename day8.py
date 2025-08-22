def reverseWords(s: str) -> str:
    # Step 1: split() trims and reduces multiple spaces automatically
    words = s.split()
    
    # Step 2: reverse the list of words
    words.reverse()
    
    # Step 3: join them with a single space
    return " ".join(words)


# -------------------
# Test Cases
# -------------------
tests = [
    "the sky is blue",        # Example 1
    "  hello world  ",        # Example 2
    "a  good   example",      # Example 3
    "   ",                    # Edge case: all spaces
    "word"                    # Edge case: single word
]

for t in tests:
    print(f"Input : \"{t}\"")
    print(f"Output: \"{reverseWords(t)}\"")
    print("-"*40)

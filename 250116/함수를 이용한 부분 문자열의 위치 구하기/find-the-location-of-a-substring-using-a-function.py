def find_substring(inp, obj):
    # If target string is longer than input string, return -1
    if len(obj) > len(inp):
        return -1
    
    # Check each possible starting position
    for i in range(len(inp) - len(obj) + 1):
        # Compare substring of input with target string
        if inp[i:i+len(obj)] == obj:
            return i
            
    # If no match is found, return -1
    return -1

# Get input
inp = input()  # Input string
obj = input()  # Target string to find

# Find and print result
result = find_substring(inp, obj)
print(result)
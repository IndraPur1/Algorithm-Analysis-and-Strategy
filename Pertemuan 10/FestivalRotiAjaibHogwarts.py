def assign_cookies(g, s):
    # Sort both lists in ascending order
    g.sort()
    s.sort()
    
    # Initialize pointers and count
    i = 0  # Pointer for children
    j = 0  # Pointer for cookies
    count = 0  # Number of satisfied children
    
    # Greedy assignment
    while i < len(g) and j < len(s):
        if s[j] >= g[i]:  # If the current cookie can satisfy the current child
            count += 1
            i += 1  # Move to the next child
            j += 1  # Move to the next cookie
        else:
            j += 1  # Current cookie is too small, try the next cookie
    
    return count

# Read input
g = list(map(int, input().split()))  # Greed factors
s = list(map(int, input().split()))  # Cookie sizes

# Compute and output the result
result = assign_cookies(g, s)
print(result)
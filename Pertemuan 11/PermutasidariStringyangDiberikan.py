def unique_permutations(S):
    # Sort the string to ensure lexicographical order
    chars = sorted(list(S))
    n = len(chars)
    result = []
    used = [False] * n
    current = []
    
    def backtrack():
        if len(current) == n:
            result.append(''.join(current))
            return
        prev = None
        for i in range(n):
            if not used[i] and chars[i] != prev:
                # Skip used characters or duplicates
                used[i] = True
                current.append(chars[i])
                backtrack()
                current.pop()
                used[i] = False
                prev = chars[i]
    
    backtrack()
    return result

# Read input
S = input().strip()

# Get and print permutations
permutations = unique_permutations(S)
for perm in permutations:
    print(perm)
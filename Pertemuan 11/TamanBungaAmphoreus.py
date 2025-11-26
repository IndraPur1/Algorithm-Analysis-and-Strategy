def canPlaceFlowers(flowerbed, n):
    # Make a copy to avoid modifying the input array
    arr = flowerbed.copy()
    count = 0
    length = len(arr)
    
    for i in range(length):
        # Check if we can place a flower at index i
        if arr[i] == 0:
            # Check previous and next positions
            prev = (i == 0 or arr[i-1] == 0)
            next_pos = (i == length-1 or arr[i+1] == 0)
            if prev and next_pos:
                arr[i] = 1  # Place a flower
                count += 1
                if count >= n:
                    return True
    return count >= n

# Read input
flowerbed = list(map(int, input().split()))
n = int(input())

# Print result as lowercase "true" or "false"
print(str(canPlaceFlowers(flowerbed, n)).lower())
def findminmax(arr):
    min = arr[0]
    max = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min:
            min = arr[i]
        if arr[i] > max:
            max = arr[i]
    return min, max

n = int(input())
arr = list(map(int, input().split()))
min_val, max_val = findminmax(arr)
print(min_val, max_val)
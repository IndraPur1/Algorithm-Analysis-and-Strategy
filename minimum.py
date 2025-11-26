def find_min(lst):
    min = lst[0]
    for i in range(1, len(lst)):
        if lst[i] < min:
            min = lst[i]
    return min

lst = input.split()
print(find_min(lst))
def pecahanuang(X):
    A = [50, 25, 10, 5, 1]
    count = 0
    for nilai in A:
        while X >= nilai:
            X -= nilai
            count += 1
    return count

X = int(input())

print(pecahanuang(X))
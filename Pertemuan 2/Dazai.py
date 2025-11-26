def Dazai(A, left = 0, right = None, memo={}):
    if right == None:
        right = len(A) - 1
    if left > right:
        return 0
    if (left, right) in memo:
        return memo[(left, right)]
    
    pickleft = A[left] - Dazai(A, left + 1, right, memo)
    pickright = A[right] - Dazai(A, left, right - 1, memo)
    memo[(left, right)] = max(pickleft, pickright)
    
    return memo[(left, right)] if left != 0 or right != len(A) - 1 else memo[(left, right)] >= 0

A = list(map(int, input().split()))
print(Dazai(A))
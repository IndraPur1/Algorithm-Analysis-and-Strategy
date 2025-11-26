def kromosom(A, i=0):
    count = 0

    if i >= len(A) - 1:
        return 0
        
    if A[i] == "X" and A[i+1] == "Y":
        count += 1
        return count + kromosom(A, i + 2)
    else:
        return kromosom(A, i + 1)
A = input().strip()
hasil = kromosom(A, 0)
print(True if hasil % 2 == 0 and hasil > 0 else False)
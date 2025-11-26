def Pyramid(A, tingkat=[]):
    if len(A) == 1:
        tingkat.append(A)
        for tingkatan in reversed(tingkat):
            print(" ".join(map(str, tingkatan)))
        return
    tingkat.append(A)
    Pyramid([A[i] + A[i + 1] for i in range(len(A) - 1)], tingkat)
    
N = int(input())
A = list(map(int, input().split()))
Pyramid(A)
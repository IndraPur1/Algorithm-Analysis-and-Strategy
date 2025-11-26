def belanjaanbudi(X, A):
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if A[i] + A[j] == X:
                return i,j
                
X = int(input())
N = int(input())
A = [int(x) for x in input().split()]

print(belanjaanbudi(X,A))

# Input
# X = 10
# N = 5
# A = 1 7 4 8 6
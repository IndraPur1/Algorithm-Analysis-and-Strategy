def Robot(N, curr = ""):
    if len(curr) == N:
        print (curr, end=" ")
        return
    Robot(N, curr + "0")
    if not curr or curr[-1] != '1':
        Robot(N, curr + "1")

N = int(input())
Robot(N)
print()
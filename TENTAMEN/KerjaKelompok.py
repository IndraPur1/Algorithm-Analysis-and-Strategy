def hitung_sum_min(N, arr):
    sum_min = 0
    ada_kurang = False    # P < L
    ada_lebih = False     # P > L
    ada_sama = False      # P = L

    min_diff_kurang = float('inf')  # min(L - P) utk P < L
    min_diff_lebih = float('inf')   # min(P - L) utk P > L
    ada_L = False      
    ada_P = False       

    for str_data in arr:
        L_i = str_data.count('L')
        P_i = str_data.count('P')

        if L_i > 0:
            ada_L = True
        if P_i > 0:
            ada_P = True

        if P_i < L_i:
            sum_min += P_i     
            ada_kurang = True
            diff = L_i - P_i
            if diff < min_diff_kurang:
                min_diff_kurang = diff
        elif P_i > L_i:
            sum_min += L_i
            ada_lebih = True
            diff = P_i - L_i
            if diff < min_diff_lebih:
                min_diff_lebih = diff
        else: # P == L
            sum_min += L_i 
            ada_sama = True

    if not ada_lebih and not ada_sama and ada_P:
        sum_min += min_diff_kurang
    elif not ada_kurang and not ada_sama and ada_L:
        sum_min += min_diff_lebih

    return sum_min

N = int(input())
arr = [input().strip() for _ in range(N)]
print(hitung_sum_min(N, arr))
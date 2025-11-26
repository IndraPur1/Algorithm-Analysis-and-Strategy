def Tom(tikus, k):
    if len(tikus) == 1:
        return tikus[0]

    pivot = tikus[0]
    tikusbesar = [x for x in tikus if x > pivot]
    tikuskecil = [x for x in tikus if x < pivot]
    tikussama = [x for x in tikus if x == pivot]

    if k <= len(tikusbesar):
        return Tom(tikusbesar, k)
    elif k <= len(tikusbesar) + len(tikussama):
        return pivot
    else:
        return Tom(tikuskecil, k - len(tikusbesar) - len(tikussama))

n, k = map(int, input().split())
tikus = list(map(int, input().split()))

print(Tom(tikus, k))
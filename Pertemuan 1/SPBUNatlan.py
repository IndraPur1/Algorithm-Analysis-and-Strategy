def spbu(gas, cost):
    total = 0
    current = 0
    start = 0
    for i in range(len(gas)):
        total = total + gas[i] - cost[i]
        current = current + gas[i] - cost[i]
        if current < 0:
            start = i + 1
            current = 0

    if total < 0:
        return -1
    else:
        return start


gas = list(map(int, input().split()))
cost = list(map(int, input().split()))

print(spbu(gas, cost))
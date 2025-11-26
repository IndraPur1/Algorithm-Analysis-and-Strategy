def max_goat_points(n, b, players):
    # Sort players by contribution-to-cost ratio in descending order
    players.sort(key=lambda x: x[0] / x[1], reverse=True)
    
    remaining_budget = b
    total_points = 0.0
    
    # Greedy selection
    for contribution, cost in players:
        if remaining_budget >= cost:
            total_points += contribution
            remaining_budget -= cost
        else:
            fraction = remaining_budget / cost
            total_points += fraction * contribution
            break
    
    return total_points

# Read input
n, b = map(int, input().split())
players = []
for _ in range(n):
    contribution, cost = map(int, input().split())
    players.append((contribution, cost))

# Compute and output the result
result = max_goat_points(n, b, players)
print("{:.2f}".format(result))
def knapsack_branch_and_bound(n, W, weights, values):
    # Create items list with index, weight, value, and value/weight ratio
    items = [(i, weights[i], values[i], values[i] / weights[i]) for i in range(n)]
    
    # Global variable to track the best value
    best_value = 0
    
    def get_upper_bound(idx, curr_weight, curr_value, remaining_capacity):
        if curr_weight > W:
            return 0
        bound = curr_value
        # Sort remaining items by value/weight ratio
        remaining = sorted(
            [(items[i][2], items[i][1]) for i in range(idx, n)],
            key=lambda x: x[0] / x[1],
            reverse=True
        )
        # Greedily add items
        for value, weight in remaining:
            if remaining_capacity >= weight:
                bound += value
                remaining_capacity -= weight
            else:
                # Add fractional part of the last item
                bound += (value / weight) * remaining_capacity
                break
        return bound
    
    def branch_and_bound(idx, curr_weight, curr_value):
        nonlocal best_value
        
        # Base case: processed all items
        if idx == n:
            best_value = max(best_value, curr_value)
            return
        
        # Prune if upper bound is not better than best_value
        if get_upper_bound(idx, curr_weight, curr_value, W - curr_weight) <= best_value:
            return
        
        # Exclude current item
        branch_and_bound(idx + 1, curr_weight, curr_value)
        
        # Include current item if weight allows
        if curr_weight + weights[idx] <= W:
            branch_and_bound(idx + 1, curr_weight + weights[idx], curr_value + values[idx])
    
    # Start Branch and Bound
    branch_and_bound(0, 0, 0)
    return best_value

# Read input
n, W = map(int, input().split())
weights = list(map(int, input().split()))
values = list(map(int, input().split()))

# Print result
print(knapsack_branch_and_bound(n, W, weights, values))
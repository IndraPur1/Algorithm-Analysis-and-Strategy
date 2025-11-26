def max_damage(S, J, H, skills):
    # Sort skills by damage in descending order
    skills.sort(key=lambda x: x[0], reverse=True)
    
    total_damage = 0
    remaining_sp = S
    
    # Select skills greedily
    for damage, sp in skills:
        if sp <= remaining_sp:
            total_damage += damage
            remaining_sp -= sp
    
    status = "KO" if total_damage >= H else "Terluka"
    return f"{total_damage} {status}"

# Input processing
S, J, H = map(int, input().split())
skills = []
for _ in range(J):
    D, P = map(int, input().split())
    skills.append((D, P))

# Output the result
print(max_damage(S, J, H, skills))
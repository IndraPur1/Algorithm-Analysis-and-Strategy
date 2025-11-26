def max_damage(S, J, H, skills):
    skills.sort(key=lambda x: x[0], reverse=True)  
    total_damage = 0
    remaining_sp = S
    for damage, sp in skills:
        if sp <= remaining_sp:
            total_damage += damage
            remaining_sp -= sp
    status = "KO" if total_damage >= H else "Terluka"
    return f"{total_damage} {status}"

S, J, H = map(int, input().split())
skills = []
for _ in range(J):
    D, P = map(int, input().split())
    skills.append((D, P))
print(max_damage(S, J, H, skills))
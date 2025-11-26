def find_anomaly_dna(s):
    n = len(s)
    a_count = 0
    t_count = 0
    c_count = 0
    g_count = 0
    
    a_diff = 0
    c_diff = 0

    min_a_diff = 0
    min_c_diff = 0

    for i in range(n):
        if s[i] == 'A':
            a_count += 1
        elif s[i] == 'T':
            t_count += 1
        elif s[i] == 'C':
            c_count += 1
        elif s[i] == 'G':
            g_count += 1

        a_diff = a_count - t_count
        c_diff = c_count - g_count

        if a_diff < min_a_diff or c_diff < min_c_diff:
            return i + 1

        min_a_diff = min(min_a_diff, a_diff)
        min_c_diff = min(min_c_diff, c_diff)

    return -1

s = input().strip()
print(find_anomaly_dna(s))

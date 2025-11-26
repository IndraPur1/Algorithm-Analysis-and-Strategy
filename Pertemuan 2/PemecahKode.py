def kode(S, index = 0, memo = {}):
    if index in memo:
        return memo[index]
    if index == len(S):
        return 1
    if S[index] == '0':
        return 0
    code = kode(S, index + 1, memo)
    if index + 1 < len(S) and '10' <= S[index:index+2] <= '26':
        code += kode(S, index + 2, memo) 
    memo[index] = code
    return code

print(kode(input().strip()))
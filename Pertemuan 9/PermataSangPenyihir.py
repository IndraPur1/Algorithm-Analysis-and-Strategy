class node:
    def _init_(self, index, count):
        self.index = index
        self.count = count
        
def Arkanastra(jewels, stones):
    n = len(stones)
    stack = [node(-1,0)]
    MaxJumlah = 0
    
    while stack:
        nodes = stack.pop()
        nextindex = nodes.index + 1
        
        if nextindex < n:
            if stones[nextindex] in jewels:
                stack.append(node(nextindex, nodes.count + 1))
                MaxJumlah = max(MaxJumlah, nodes.count + 1)
            stack.append(node(nextindex, nodes.count))
        
    return MaxJumlah

jewels = input().strip()
stones = input().strip()
print(Arkanastra(jewels, stones))
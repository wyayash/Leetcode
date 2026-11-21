class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)
        last = [-1] * 26
        new_parent = parent[:]
        order = []
        stack = [(0, -1, False)]
        while stack:
            node, saved, exiting = stack.pop()
            c = ord(s[node]) - 97
            if exiting:
                last[c] = saved
                continue
            saved = last[c]
            if saved != -1:
                new_parent[node] = saved  
            last[c] = node
            order.append(node)
            stack.append((node, saved, True))
            for ch in children[node]:
                stack.append((ch, -1, False))
        size = [1] * n
        for x in reversed(order):
            if x != 0:
                size[new_parent[x]] += size[x]
        return size
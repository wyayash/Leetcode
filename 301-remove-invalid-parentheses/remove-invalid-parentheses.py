from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def is_valid(s):
            balance=0
            for c in s:
                if c=='(':
                    balance+=1
                elif c==')':
                    balance-=1
                if balance<0:
                    return False
            return balance==0
        queue=deque([s])
        visited={s}
        found=False
        ans=[]
        while queue:
            curr=queue.popleft()
            if is_valid(curr):
                ans.append(curr)
                found=True
            if found:
                continue
            for i in range(len(curr)):
                if curr[i] not in "()":
                    continue
                new_s=curr[:i]+curr[i+1:]
                if new_s not in visited:
                    visited.add(new_s)
                    queue.append(new_s)
        return ans
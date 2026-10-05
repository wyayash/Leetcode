class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[0]
        for c in s:
            if c=='(':
                stack.append(0)
            else:
                curr=stack.pop()
                if curr==0:
                    curr=1
                else:
                    curr*=2
                stack[-1]+=curr
        return stack[0]
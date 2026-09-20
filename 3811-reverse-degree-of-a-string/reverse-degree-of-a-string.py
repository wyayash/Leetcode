class Solution:
    def reverseDegree(self, s: str) -> int:
        ans=0
        for i,c in enumerate(s):
            value=26-(ord(c)-ord('a'))
            ans+=value*(i + 1)
        return ans
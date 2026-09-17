class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n=len(arr)
        ps=0
        res=inf
        dp=[inf]*n
        l=0
        for r in range(n):
            ps +=arr[r]
            while ps>target:
                ps-=arr[l]
                l+=1
            dp[r]=dp[r-1] if r-1 >=0 else inf
            if ps==target:
                res= min(res,r-l+1+(dp[l-1] if l-1 >=0 else inf))
                dp[r] = min(dp[r], r-l+1)
        return -1 if res == inf else res
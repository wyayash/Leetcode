from functools import lru_cache
from typing import List
class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m,n=len(grid),len(grid[0])
        if (m+n-1)%2==1:
            return False
        if grid[0][0]==')' or grid[m-1][n- 1] =='(':
            return False
        @lru_cache(None)
        def dfs(r,c,balance):
            balance+=1 if grid[r][c]=='(' else -1
            if balance<0:
                return False
            if r==m-1 and c==n-1:
                return balance==0
            if r+1<m and dfs(r+1,c,balance):
                return True
            if c+1<n and dfs(r, c+1,balance):
                return True
            return False
        return dfs(0, 0,0)
class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str,
                       queries: list[str]) -> list[bool]:
        adj=[[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        LOG=max(1,n.bit_length())
        up=[[0]*n for _ in range(LOG)]
        depth=[0]*n
        tin=[0]*n
        tout=[0]*n
        base=[0]*n
        chars=[1<<(ord(c)-97) for c in s]

        timer =0
        base[0]=chars[0]
        tin[0]=0
        timer=1
        stack=[(0,0)] 
        while stack:
            node,idx=stack[-1]
            if idx<len(adj[node]):
                stack[-1]=(node,idx+1)
                nxt=adj[node][idx]
                if nxt==up[0][node] and node != 0 or (node==0 and False):
                    continue
                if node!=0 and nxt==up[0][node]:
                    continue
                up[0][nxt]=node
                depth[nxt]=depth[node]+1
                base[nxt]=base[node]^chars[nxt]
                tin[nxt]=timer
                timer+=1
                stack.append((nxt,0))
            else:
                tout[node]=timer-1
                stack.pop()
        for j in range(1,LOG):
            prev,cur=up[j-1],up[j]
            for v in range(n):
                cur[v]=prev[prev[v]]
        def lca(a:int,b:int)->int:
            if depth[a]<depth[b]:
                a,b=b,a
            diff=depth[a]-depth[b]
            for j in range(LOG):
                if diff>>j&1:
                    a=up[j][a]
            if a==b:
                return a
            for j in range(LOG-1,-1,-1):
                if up[j][a]!=up[j][b]:
                    a=up[j][a]
                    b=up[j][b]
            return up[0][a]

        size=n +2
        bit=[0]*(size+1)

        def upd(i:int,d:int)->None:
            i+=1
            while i<=size:
                bit[i]^=d
                i+=i&-i

        def qry(i:int)->int:
            i+=1
            r=0
            while i>0:
                r^= bit[i]
                i-=i &-i
            return r

        cur_chars=chars[:]
        ans=[]
        for q in queries:
            parts=q.split()
            if parts[0]=="update":
                u=int(parts[1])
                new=1<<(ord(parts[2])-97)
                delta=cur_chars[u]^new
                if delta:
                    upd(tin[u],delta)
                    upd(tout[u]+1,delta)
                    cur_chars[u]=new
            else:
                u,v=int(parts[1]),int(parts[2])
                w=lca(u, v)
                m=(base[u]^qry(tin[u]))^(base[v]^qry(tin[v]))^ cur_chars[w]
                ans.append(m& (m-1)==0)
        return ans
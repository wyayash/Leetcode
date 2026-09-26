class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        mp=dict(knowledge)
        res=[]
        i=0
        while i<len(s):
            if s[i]=="(":
                j=i+1
                while s[j]!=")":
                    j+=1
                key=s[i+1:j]
                res.append(mp.get(key,"?"))
                i=j+1
            else:
                res.append(s[i])
                i+=1
        return "".join(res)
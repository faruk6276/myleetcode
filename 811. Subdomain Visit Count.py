class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        h={}
        for st in cpdomains:
            st=st.split(" ")
            dom=st[1].split(".")
            v=""
            for x in range(len(dom)-1,-1,-1):
                if x==len(dom)-1:
                    v=dom[x]
                else:
                    v=dom[x]+"."+v
                if v in h:
                    h[v]+=int(st[0])
                else:
                    h[v]=int(st[0])
        cp=[]
        for key,val in h.items():
            cp.append(str(val)+" "+key)
        return cp
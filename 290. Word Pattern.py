class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dict_onary={}
        s=s.split()
        if len(pattern) != len(s) or len(set(s))!=len(set(pattern)):
            return False
        for index,val in enumerate(pattern):
            if val in dict_onary:
                if dict_onary[val]!=s[index]:return False
            else:
                dict_onary[val]=s[index]
        return True
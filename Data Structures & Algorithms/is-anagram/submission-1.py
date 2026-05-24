class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''if (len(s) != len(t)):
            return False
        for ss in s:
            if ss not in t:
                return False
        return True'''
        return sorted(s) == sorted(t)
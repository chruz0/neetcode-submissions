class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        set1 = set(s)
        set2 = set(t)
        return set1 == set2
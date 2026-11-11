class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        list1 = list(s)
        list2 = list(t)
        for v in list1:
            if v not in list2:
                pass
        set1 = set(s)
        set2 = set(t)
        if set1 == set2:
            return True
        return False
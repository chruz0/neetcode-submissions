class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        timesseen1 = {}
        timesseen2 = {}
        if len(s) != len(t):
            return False
        list1 = list(s)
        list2 = list(t)
        for v in list1:
            if v not in timesseen1:
                timesseen1[v] = 1
            else:
                timesseen1[v] += 1
        
        for w in list2:
            if w not in timesseen2:
                timesseen2[w] = 1
            else:
                timesseen2[w] += 1
        if timesseen1 == timesseen2:
            return True
        else:
            return False
        set1 = set(s)
        set2 = set(t)
        if set1 == set2:
            return True
        return False
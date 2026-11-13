class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # (1) check for size equivalence first...
            return False
        timesseen1 = {} # (1) ...then create dictionaries
        timesseen2 = {}
        for v in s: # (2) no need for lists, strings are iterable
            if v not in timesseen1:
                timesseen1[v] = timesseen1.get(v, 0) + 1 # (3) look for v, if not there, add the key, default to 0, then add 1 to the value
        
        for w in t: # (2)
            if w not in timesseen2:
                timesseen2[w] = timesseen2.get(w, 0) + 1 # (3)

        return timesseen1 == timesseen2 # (4) no need for if statements if only returning True/False
        # (5) removed older code that was 
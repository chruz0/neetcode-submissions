class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #list1 = ["hi"]
        #list2 = [list1]
        #return list2

        if len(strs) == 1:
            return [strs]


        for strn in strs:
            timesseen = {}
            for v in strn:
                timeseen[v] = timeseen.get(v,0) + 1

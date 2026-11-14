class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if len(strs) == 1:
            return [strs]
        
        evalwords = {}
        sortstrs = []
        anagrams = []

#        for i, strn in enumerate(strs):
 #           timesseen = {}
  #          for v in strn:
   #             timesseen[v] = timesseen.get(v,0) + 1
    #        evalwords[strn] = timesseen
     #   
      #  for strn in evalwords:
      
        for strn in strs:
            sortstrs.append("".join(sorted(strn)))

        for i, strn in enumerate(sortstrs):
            if strn not in evalwords:
                evalwords[strn] = [strs[i]]
            else:
                evalwords[strn].append(strs[i])
            
        for key, val in evalwords.items():
            anagrams.append(val)
        
        return anagrams
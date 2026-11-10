class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        if output == []:
            for i, v1 in enumerate(nums):
                if output == []:
                    for j, v2 in enumerate(nums):
                        if output == []:
                            if i==j:
                                continue
                            if v1 + v2 == target:
                                output.append(i)
                                output.append(j)     
        return output
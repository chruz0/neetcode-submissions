class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = []
        for i, v1 in enumerate(nums):
            for j, v2 in enumerate(nums):
                if i == j:
                    continue
                if v1 == v2:
                    return True
        return False
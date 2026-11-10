class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i, v in enumerate(nums):
            if v not in seen:
                seen.add(v)
            else:
                return True
        return False
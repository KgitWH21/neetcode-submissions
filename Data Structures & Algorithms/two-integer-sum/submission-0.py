class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for idx, num in enumerate(nums):
            comp = target - num
            if comp in nums:
                comp_idx = nums.index(comp)
                if comp_idx != idx:
                    return sorted([idx, comp_idx])
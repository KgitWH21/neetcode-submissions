from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)
        print(counts)
        majority = counts.most_common(1)
        print(majority)
        most_freq = majority[0][0]

        return most_freq

 
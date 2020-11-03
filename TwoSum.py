#TC:- O(n)
#SC:- O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h={}
        for i, val in enumerate(nums):
            n=target-val
            if n not in h:
                h[val]=i
            else:
                return [h[n],i]

from collections import defaultdict
from typing import List
import pdb

class Solution :
    def singleNumber(self, nums: List[int]) -> int :
        pdb.set_trace()
        hash_table = defaultdict(int)
        for i in nums :
            hash_table[i] += 1

        for i in hash_table :
            if hash_table[i] == 1 :
                return i

print(Solution().singleNumber([2,2,1]))
"""
class Solution:
    def singleNumber(self,nums):
        single_num = 0
        for i in range(0,len(nums)):
            count = 0
            for j in range(0,len(nums)):
                if nums[i]==nums[j]:
                    count += 1
                    continue
                else:
                    continue
            if count==1:
                single_num = nums[i]
        return single_num   


print(Solution().singleNumber([2,2,1]))
"""
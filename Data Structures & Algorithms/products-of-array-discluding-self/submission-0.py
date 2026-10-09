import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lists = []
        for i in range(len(nums)):
            index_to_remove = i
            new_list = nums[:index_to_remove] + nums[index_to_remove+1:]
            #print(math.prod(nums))
            lists.append(math.prod(new_list))
        return (lists)


        
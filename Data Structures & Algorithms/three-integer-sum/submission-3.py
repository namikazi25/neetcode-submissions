class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #result = []
        final_result = set()
        nums.sort()
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    result = tuple(sorted((nums[i], nums[j], nums[k])))
                    final_result.add(result)
                    j += 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1
        return [list(triplet) for triplet in final_result] 

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max = 0
        for i in range (0,(len(nums))):
            if 1 == nums[i]:
                count = count + 1
                print(count)
                if max < count: 
                    max = count
            else: 
                count = 0
                print(count)
        return max
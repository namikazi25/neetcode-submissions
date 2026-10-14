class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(list)
        for s in nums:
            res[s].append(s)
        res = sorted(res, key=lambda s: len(res[s]), reverse=True)

        result = []
        for s in res: 
            print(s)
            result.append(s)
        return result[:k]            
            

        


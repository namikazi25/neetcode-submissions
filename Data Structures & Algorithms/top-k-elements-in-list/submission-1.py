class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        char_count = {}
        for num in nums:
            char_count[num] = char_count.get(num, 0) + 1

        # keys_with_value_k = [key for key, value in char_count.items() if value >= k]
        sorted_keys = sorted(char_count.keys(), key=lambda x: char_count[x], reverse=True)
        
        return sorted_keys[:k]
                
        
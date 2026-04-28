class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}       
        for e in nums:
            freq_dict[e] = freq_dict.get(e,0) + 1

            sorted_nums = sorted(freq_dict, key=freq_dict.get, reverse=True)
        return sorted_nums[:k]


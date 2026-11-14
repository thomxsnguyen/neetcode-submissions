class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:  
        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        bucketSort = [0] * len(freq)

        for key, value in freq.items():
            bucketSort[value] = key
        
        print(bucketSort)

        return []

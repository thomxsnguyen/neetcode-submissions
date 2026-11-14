class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:  
        bucketSort = [0] * len(nums)
        freq = {}
        output = []
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
    

        for key, value in freq.items():
            bucketSort[value] = key
        print(bucketSort)

        return []

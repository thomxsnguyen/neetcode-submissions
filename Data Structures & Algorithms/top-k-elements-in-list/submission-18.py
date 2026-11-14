class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:  
        freq = {}
        bucketSort = ['_' for i in range(len(nums) + 1)]
        output = []
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
    
        for key, value in freq.items():
            bucketSort[value] = key
        
        for i in range(len(bucketSort) - 1, -1, -1):
            if bucketSort[i] != '_':
                output.append(bucketSort[i])
            if len(output) >= k:
                return output

        return output

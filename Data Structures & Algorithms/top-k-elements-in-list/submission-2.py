class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        heap = []
        
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))

            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []

        for num in heap:
            result.append(num[1])
            
        return result
            



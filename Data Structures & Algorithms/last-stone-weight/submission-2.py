class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq

        heap = []

        for stone in stones:
            heapq.heappush(heap, -stone)

        while len(heap) >= 2:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)
            difference = first - second
            heapq.heappush(heap, difference)
            
        
        if heap:
            return -heap[0]
        return heap
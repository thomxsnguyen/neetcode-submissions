class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq

        heap = []

        for stone in stones:
            heapq.heappush(heap, -stone)

        while len(heap) >= 2:
            first = heap[0]
            second = heap[-1]
            difference = first - second
            heapq.heappush(heap, difference)
            heapq.heappop(heap)
            heapq.heappop(heap)
        
        if heap:
            return -heap[0]
        return heap
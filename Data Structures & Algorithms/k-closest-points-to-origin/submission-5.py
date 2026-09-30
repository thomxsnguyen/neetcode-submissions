class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        heap = []
        result = []
        for x, y in points:
            heapq.heappush(heap, (x**2 + y**2, x, y))
        print(heap)
        for i in range(k):
            distance, x, y = heapq.heappop(heap)
            result.append([x, y])
        print(result)
        return result
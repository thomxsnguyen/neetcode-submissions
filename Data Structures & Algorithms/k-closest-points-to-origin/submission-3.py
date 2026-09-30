class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        heap = []
        result = []
        for x, y in points:
            heapq.heappush(heap, (x**2 + y**2, x, y))
        print(heap)
        for i in range(k):
            result.append((heap[i][1], heap[i][2]))
        print(result)
        return result
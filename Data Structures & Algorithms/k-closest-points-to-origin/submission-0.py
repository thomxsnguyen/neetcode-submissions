class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        heap = []
        result = []
        for x, y in points:
            heapq.heappush(heap, (x**2 + y**2, x, y))
        print(heap)
        print(heap[0][1])
        for i in range(k - 1):
            result.append((heap[i][1], heap[i][0]))
        
        print(result)
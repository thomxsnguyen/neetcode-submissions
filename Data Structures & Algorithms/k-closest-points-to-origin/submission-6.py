class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        heap = [] #O(n)
        result = [] #o(k)
        for x, y in points: #o(n)
            heapq.heappush(heap, (x**2 + y**2, x, y)) #o(logn)
        for i in range(k):#o(k)
            distance, x, y = heapq.heappop(heap) #o(logk)
            result.append([x, y])

        return result

        #space complexity O(n + k) or o(n)
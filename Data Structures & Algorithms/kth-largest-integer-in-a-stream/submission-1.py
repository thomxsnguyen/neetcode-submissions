class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums


    def add(self, val: int) -> int:
        import heapq
        
        self.nums.append(val)
        
        heap = []

        for num in self.nums:
            heapq.heappush(heap, num)
            if len(heap) > self.k:
                heapq.heappop(heap)
        
        return heap[0]
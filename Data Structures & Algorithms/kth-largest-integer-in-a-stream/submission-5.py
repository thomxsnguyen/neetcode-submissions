class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        import heapq
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)

        while len(self.heap) > k:
            heapq.heappop(self.heap)


    def add(self, val: int) -> int:
    
        
        self.heap.append(val)
        
        return heap[0]
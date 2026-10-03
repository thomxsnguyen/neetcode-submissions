class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heap.heapify(self.heap)

        while len(heap) > k:
            heapq.heappop(heap)


    def add(self, val: int) -> int:
        import heapq
        
        self.heap.append(val)
        
        return heap[0]
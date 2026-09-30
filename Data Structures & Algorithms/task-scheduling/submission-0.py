class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import deque
        import heapq

        count = {}
        queue = deque([])
        for task in tasks:
            count[task] = count.get(task, 0) + 1


        heap = []
        
        for task, freq in count.items():
            heapq.heappush(heap, -freq)

        time = 0

        while heap or queue:
            time += 1

            if queue and queue[0][1] == time:
                freq, ready_time = queue.popleft()
                heapq.heappush(heap, freq)
            
            if heap:
                freq = heapq.heappop(heap)
                freq += 1

                if freq != 0:
                    ready_time = time + n + 1
                    queue.append((freq, ready_time))
        
        return time

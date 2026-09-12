class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        max_heap = [-freq for freq in count.values()]

        heapq.heapify(max_heap)
        time = 0
        queue = deque()

        while max_heap or queue:
            time += 1

            if max_heap:
                freq = heapq.heappop(max_heap)
                freq += 1

                if freq != 0:
                    queue.append((freq,time + n))

            if queue and queue[0][1] == time:
                freq, ready_time = queue.popleft()
                heapq.heappush(max_heap, freq)
        
        return time
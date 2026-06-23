class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # process most common task first
        # record the time it was processed
        cycle = 0
        h = [-c for c in Counter(tasks).values()]
        heapq.heapify(h)
        idle = deque() # (count, min time to be processed)

        while h or idle:
            cycle += 1
            if h:
                # pop from heap and process the task
                count = heapq.heappop(h) + 1
                # if still task left, put it in the idle q
                if count < 0:
                    idle.append((count, cycle + n))
            else:
                cycle = idle[0][1]
            
            while idle and idle[0][1] <= cycle:
                heapq.heappush(h, idle.popleft()[0])

        return cycle
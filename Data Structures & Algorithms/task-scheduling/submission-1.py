class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # the most common task first
        counter = Counter(tasks) # key: task, val: count
        h = [-c for c in counter.values()] # track the most common tsk count
        heapq.heapify(h)
        q = deque() # list of ideling tasks; (-count, time to idle)
        time = 0

        while h or q:
            time += 1
            if not h: time = q[0][1] # all tasks are ideling
            else:
                count = heapq.heappop(h) + 1
                if count < 0:
                    q.append((count, time + n))

            # when the time in queue came, add back to heap
            if q and q[0][1] == time:
                heapq.heappush(h, q.popleft()[0])

        return time

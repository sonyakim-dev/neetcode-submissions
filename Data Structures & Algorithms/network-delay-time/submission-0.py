class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # n: number of nodes, k: start point
        # Djikstra (BFS, min heap), weighed graph
        graph = defaultdict(list) # key: node1, val: (node2, time)
        h = [(0, k)] # (travel distance, node)
        visited = {}

        for n1, n2, t in times:
            graph[n1].append((n2, t))

        while h:
            time, node = heapq.heappop(h)
            if node not in visited:
                visited[node] = time
                for neigh, weight in graph[node]:
                    heapq.heappush(h, (time + weight, neigh))\

        return max(visited.values()) if len(visited) == n else -1
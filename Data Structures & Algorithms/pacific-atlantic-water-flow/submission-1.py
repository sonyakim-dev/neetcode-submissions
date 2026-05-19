class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        row, col = len(heights), len(heights[0])
        pac, atl = set(), set()
        result = []

        def dfs(r, c, visited):
            visited.add((r, c))
            for dr, dc in direction:
                R, C = dr + r, dc + c
                if R in range(row) and C in range(col)\
                    and (R, C) not in visited and heights[R][C] >= heights[r][c]:
                    dfs(R, C, visited)
        
        for r in range(row):
            dfs(r, 0, pac)
            dfs(r, col-1, atl)

        for c in range(col):
            dfs(0, c, pac)
            dfs(row-1, c, atl)

        return list(pac.intersection(atl))
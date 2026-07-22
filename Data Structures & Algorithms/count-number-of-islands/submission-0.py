import collections

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))

            while q:
                # Use the coordinates popped from the queue!
                curr_r, curr_c = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    nr, nc = curr_r + dr, curr_c + dc
                    # Optimized boundary and condition checks
                    if (0 <= nr < rows and 0 <= nc < cols and 
                        grid[nr][nc] == "1" and (nr, nc) not in visit):
                        q.append((nr, nc))
                        visit.add((nr, nc))

        for r in range(rows):
            for c in range(cols):
                # Ensure we only start BFS on unvisited land
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
        
        return islands
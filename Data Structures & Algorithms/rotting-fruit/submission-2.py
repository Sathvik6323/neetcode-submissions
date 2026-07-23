from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = deque()
        fresh_count = 0  # FIX 1: Track count of fresh oranges

        def addrotten(r, c):
            nonlocal fresh_count
            if r < 0 or c < 0 or r == rows or c == cols or grid[r][c] == 0 or (r, c) in visit:
                return
            grid[r][c] = 2
            visit.add((r, c))
            q.append([r, c])
            fresh_count -= 1  # Decrement fresh oranges remaining

        # Initial scan to find all rotten oranges and count fresh ones
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r, c])
                    visit.add((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1

        # FIX 2: If there are no fresh oranges to rot, return 0 immediately
        if fresh_count == 0:
            return 0

        time = 0  # Start time at 0
        
        # Standard Multi-Source BFS
        while q and fresh_count > 0:  # Stop when queue is empty OR no fresh left
            for _ in range(len(q)):
                r, c = q.popleft()
                addrotten(r + 1, c)
                addrotten(r - 1, c)
                addrotten(r, c + 1)
                addrotten(r, c - 1)
            time += 1  # Increment time only after a full layer/minute finishes rottening

        # If fresh oranges remain that couldn't be reached
        return time if fresh_count == 0 else -1
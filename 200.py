from typing import List
from collections import deque

class Solution:
    """
    >>> Solution().numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])
    1
    >>> Solution().numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])
    3
    >>> Solution().numIslands([["0","1","0"],["1","0","1"],["0","1","0"]])
    4
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        height = len(grid)
        width = len(grid[0])
        def within_bounds(r, c):
            return 0 <= r and r < height and 0 <= c and c < width
        visited = [[False for _ in range(width)] for _ in range(height)]
        def unvisited_land(r, c):
            return grid[r][c] == "1" and not visited[r][c]
        def surrounding(r, c):
            yield r + 1, c
            yield r - 1, c
            yield r, c + 1
            yield r, c - 1
        islands = 0
        for row in range(height):
            for col in range(width):
                if not unvisited_land(row, col):
                    continue
                islands += 1
                q = deque()
                q.append((row, col))
                visited[row][col] = True
                while len(q) > 0:
                    r, c = q.popleft()
                    for nr, nc in surrounding(r, c):
                        if within_bounds(nr, nc) and unvisited_land(nr, nc):
                            q.append((nr, nc))
                            visited[nr][nc] = True
        return islands

if __name__ == "__main__":
    import doctest
    doctest.testmod()

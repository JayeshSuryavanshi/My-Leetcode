class Solution:
	def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
		row, col = len(maze), len(maze[0])
		visited, steps = set([]), 0
		queue = deque([entrance])

		answer = set([(0,y) for y in range(0,col) if maze[0][y] == "."] + [(row-1,y) for y in range(0,col) if maze[row-1][y] == "."] + [(x,0) for x in range(1,row-1) if maze[x][0] == "."] + [(x,col-1) for x in range(1,row-1) if maze[x][col-1] == "."])

		while queue:
			for _ in range(len(queue)):
				x, y = queue.popleft()
				if (x,y) in visited: continue
				visited.add((x,y))
				for nx, ny in [[x-1,y],[x+1,y],[x,y+1],[x,y-1]]:
					if 0<=nx<row and 0<=ny<col and maze[nx][ny] == ".":
						if (nx,ny) in answer and (nx,ny) not in visited: return steps+1
						queue.append((nx,ny))     
			steps+=1

		return -1

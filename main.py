from collections import deque

N, M = list(map(int, input().split()))
field = []
visited = deque([(0,0)])
result = 1
for i in range(N):
	tlist = list(map(int, input()))
	field.append(tlist)
	print()

print("field",field)

def bfs(visited):
	while len(visited) or visited.pop > 0:
		position = visited.popleft()
		if position == (N-1,M-1) :
			return field[position[0]][position[1]]
		
		x, y = position[0], position[1]
		
		down = (x+1, y)
		up = (x-1, y)
		left = (x, y-1)
		right = (x, y+1)
		print("now", position,end=" ")
		if x+1 < N and field[x+1][y]==1 and down not in visited:
			print("go down")
			visited.append(down)
			field[x+1][y]=field[x][y]+1
		if x-1 >= 0 and field[x-1][y]==1 and up not in visited:
			print("go up")
			visited.append(up)
			field[x-1][y]=field[x][y]+1
		if y+1 < M and field[x][y+1]==1 and right not in visited:
			print("go right")
			visited.append(right)
			field[x][y+1]=field[x][y]+1
		if y-1 >= 0 and field[x][y-1]==1 and left not in visited:
			print("go left")
			visited.append(left)
			field[x][y-1]=field[x][y]+1
		print(visited, "step=", field[x][y])
	return field[x][y]

print(bfs(visited))
N, M = list(map(int, input().split()))
field = []
notVisited=[[]*N for i in range(M-1)]
visited = [(0,0)]
result = 0
for i in range(N):
	for j in range(M):
		if i != N:
			notVisited[i].append((i,j))
	tlist = list(map(int, input()))
	field.append(tlist)
	print()

print("notvisited",notVisited)
print("field",field)
input()

def bfs(visited):
	while len(visited) > 0:
		position = visited.pop()
		
		global result
		result+=1
	
		if position == (N,M) :
			return result
		
		x, y = position[0], position[1]
		down = (x+1, y)
		up = (x-1, y)
		left = (x, y-1)
		right = (x, y+1)
		
		if x+1 < N and field[x+1][y]==1 and down not in visited:
			visited.append(down)
		if x-1 > 0 and field[x-1][y]==1 and up not in visited:
			visited.append(up)
		if y+1 < M and field[x][y+1]==1 and right not in visited:
			visited.append(right)
		if y-1 > 0 and field[x][y-1]==1 and left not in visited:
			visited.append(left)
		print(visited)
bfs(visited)
print(result)
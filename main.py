N, M = list(map(int, input().split()))
field = []
notVisited=[]
visited = [(0,0)]
result = 0
for i in range(N):
	for j in range(M):
		if i != N:
			notVisited.append((i,j))
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
	
		if position == (N-1,M-1) :
			break
			return result
		
		x, y = position[0], position[1]
		down = (x+1, y)
		up = (x-1, y)
		left = (x, y-1)
		right = (x, y+1)
		
		if x+1 < N and field[x+1][y]==1 and down not in visited:
			print("go down")
			visited.append(down)
			field[x+1][y]=0
		if x-1 > 0 and field[x-1][y]==1 and up not in visited:
			print("go up")
			visited.append(up)
			field[x-1][y]=0
		if y+1 < M and field[x][y+1]==1 and right not in visited:
			print("go right")
			visited.append(right)
			field[x][y+1]=0
		if y-1 > 0 and field[x][y-1]==1 and left not in visited:
			print("go left")
			visited.append(left)
			field[x][y-1]=0
		print(visited)
bfs(visited)
print(result)
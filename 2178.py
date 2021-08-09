'''
문제
N×M크기의 배열로 표현되는 미로가 있다.

1	0	1	1	1	1
1	0	1	0	1	0
1	0	1	0	1	1
1	1	1	0	1	1

미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 
이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 
한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 
칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

입력
첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.

출력
첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.

예제 입력 1
4 6
101111
101010
101011
111011

예제 출력 1
15
'''

# 입력처리
N, M = map(int, input().split())
maze = []
for _ in range(N):
    # 각각의 수들은 붙어서 입력이 주어진다.
    maze.append([int(i) for i in input()])

# 최단 거리를 구하기 위해서 BFS로 풀이 (출발: [0, 0], 목적지: [N - 1, M - 1])
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start[0]][start[1]] = True
    while queue:
        x, y = queue.popleft()
        for nx, ny in [[x, y - 1], [x, y + 1], [x + 1, y], [x - 1, y]]:
            if (nx in range(N)) and (ny in range(M)) and (visited[nx][ny] == False) and (graph[nx][ny] != 0):
                queue.append([nx, ny])
                visited[nx][ny] = True
                graph[nx][ny] = graph[x][y] + 1
                if (nx == N - 1) and (ny == M - 1):
                    return graph[nx][ny]
        
# visited 배열 생성
visited = [[False] * (M) for _ in range(N)]

print(bfs(maze, [0, 0], visited))
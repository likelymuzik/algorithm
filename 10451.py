'''
문제
1부터 N까지 정수 N개로 이루어진 순열을 나타내는 방법은 여러 가지가 있다. 
예를 들어, 8개의 수로 이루어진 순열 (3, 2, 7, 8, 1, 4, 5, 6)을 배열을 이용해 표현하면  															 
(1	2	3	4	5	6	7	8	
 3	2	7	8	1	4	5	6 )
 와 같다. 또는, Figure 1과 같이 방향 그래프로 나타낼 수도 있다.

Figure 1에 나와있는 것 처럼, 순열 그래프 (3, 2, 7, 8, 1, 4, 5, 6) 에는 총 3개의 사이클이 있다. 
이러한 사이클을 "순열 사이클" 이라고 한다.

N개의 정수로 이루어진 순열이 주어졌을 때, 순열 사이클의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 
각 테스트 케이스의 첫째 줄에는 순열의 크기 N (2 ≤ N ≤ 1,000)이 주어진다. 
둘째 줄에는 순열이 주어지며, 
각 정수는 공백으로 구분되어 있다.

출력
각 테스트 케이스마다, 입력으로 주어진 순열에 존재하는 순열 사이클의 개수를 출력한다.

예제 입력
2
8
3 2 7 8 1 4 5 6
10
2 1 3 4 5 6 7 9 10 8

예제 출력
3
7
'''

def dfs(graph, v, visited, cycle):
    visited[v] = True
    if not visited[graph[v]]:
        visited[graph[v]] = True
        cycle.append(graph[v])
        return dfs(graph, graph[v], visited, cycle)
    else:
        return 1

T = int(input())
for _ in range(T):
    N = int(input())
    graph = [0] + list(map(int, input().split()))
    visited = [False] * (N + 1)
    result = 0
    for i in range(1, N + 1):
        if visited[i] == False:
            result += dfs(graph, i, visited, [])
    print(result)
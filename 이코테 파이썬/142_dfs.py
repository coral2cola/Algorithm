# graph는 그래프.. 각 노드에 대해 인접한 노드의 정보를 담고 있음

# ** graph **
# 1 -> 2, 3, 8
# 2 -> 1, 7
# 3 -> 1, 4, 5
# .. 이런 식

# v는 노드의 번호를 의미
# visited 는 각 노드에 방문했는지를 표시하는 list임.

# 만약 v가 1 이라면 1번 노드를 방문했으니
# visited[1] = True 로 만들어 방문함을 표시함
# 그리고 graph[1] 에 있는 2, 3, 8 을 탐색하면서 이 중 방문하지 않은 노드에 대해
# dfs 함수를 다시 호출하는 방식.


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

dfs(graph, 1, visited)
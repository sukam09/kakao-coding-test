from collections import defaultdict


def solution(info, edges):
    ans = 0
    status = [0, 0]
    n = len(info)
    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [1] + [0] * (n - 1)
    stack = [0]
    while stack:
        v = stack.pop()
        status[info[v]] += 1
        for nv in graph[v]:
            if visited[nv]:


print(
    solution(
        [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
        [
            [0, 1],
            [1, 2],
            [1, 4],
            [0, 8],
            [8, 7],
            [9, 10],
            [9, 11],
            [4, 3],
            [6, 5],
            [4, 6],
            [8, 9],
        ],
    )
)

import sys

sys.setrecursionlimit(10**6)


def backtrack(node, cnt, n, visited, locks, keys, graph, unlocked):
    print(node, cnt, visited, locks, keys)
    global ans

    if cnt == n:
        ans = True
        return

    for next_node in graph[node]:
        if visited[next_node] or locks[next_node]:
            continue

        target = keys[next_node]
        visited[next_node] = True
        if target != -1:
            locks[target] = False
            unlocked.append(target)

        backtrack(next_node, cnt + 1, n, visited, locks, keys, graph, unlocked)

    # for unlocked_node in unlocked:
    #     backtrack(unlocked_node, cnt + 1, n, visited, locks, keys, graph, unlocked)


def solution(n, path, order):
    global cnt, ans
    graph = [[] for _ in range(n)]
    for a, b in path:
        graph[a].append(b)
        graph[b].append(a)

    visited = [True] + [False] * (n - 1)
    cnt = 1
    ans = False
    locks = [False] * n
    keys = [-1] * n
    for first, second in order:
        locks[second] = True
        keys[first] = second

    backtrack(0, cnt, n, visited, locks, keys, graph, [])
    return ans


# print(solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[8,5],[6,7],[4,1]]))
# print(solution(9, [[8,1],[0,1],[1,2],[0,7],[4,7],[0,3],[7,5],[3,6]], [[4,1],[5,2]]))
print(
    solution(
        9,
        [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]],
        [[4, 1], [8, 7], [6, 5]],
    )
)

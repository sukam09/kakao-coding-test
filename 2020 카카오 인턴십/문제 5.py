def solution(n, path, order):
    graph = [[] for _ in range(n)]
    before = [-1] * n
    after = [-1] * n
    visited = [0] * n
    stack = [0]

    for a, b in path:
        graph[a].append(b)
        graph[b].append(a)

    for a, b in order:
        if b == 0:
            return False
        before[b] = a

    while stack:
        cur = stack.pop()
        if before[cur] != -1 and not visited[before[cur]]:
            after[before[cur]] = cur
            continue

        visited[cur] = 1
        for next_ in graph[cur]:
            if visited[next_]:
                continue
            stack.append(next_)

        if after[cur] != -1:
            stack.append(after[cur])

    return sum(visited) == n

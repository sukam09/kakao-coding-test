from collections import deque


def oob(x, y, n):
    return x < 0 or x >= n or y < 0 or y >= n


def solution(board):
    n = len(board)
    # 방향 순서: 하, 우, 상, 좌
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    costs = [[[float("inf")] * 4 for _ in range(n)] for _ in range(n)]
    costs[0][0] = [0] * 4
    queue = deque([(0, 0, 0), (0, 0, 1)])

    while queue:
        x, y, dir_ = queue.popleft()
        cost = costs[x][y][dir_]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            next_cost = cost + 100 + 500 * (i != dir_)
            if oob(nx, ny, n) or board[nx][ny] == 1 or next_cost >= costs[nx][ny][i]:
                continue
            costs[nx][ny][i] = next_cost
            queue.append((nx, ny, i))

    return min(costs[n - 1][n - 1])

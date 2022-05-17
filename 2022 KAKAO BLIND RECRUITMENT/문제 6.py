def solution(board, skill):
    n, m = len(board), len(board[0])
    ans = 0

    for type_, r1, c1, r2, c2, degree in skill:
        sign = -1 if type_ == 1 else 1
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                board[i][j] += degree * sign

    for i in range(n):
        for j in range(m):
            if board[i][j] >= 1:
                ans += 1

    return ans


print(
    solution(
        [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]],
        [
            [1, 0, 0, 3, 4, 4],
            [1, 2, 0, 2, 3, 2],
            [2, 1, 0, 3, 1, 2],
            [1, 0, 1, 3, 3, 1],
        ],
    )
)
print(
    solution(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]],
    )
)

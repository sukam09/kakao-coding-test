def solution(board, moves):
    n = len(board)
    basket = []
    ans = 0

    for move in moves:
        j = move - 1
        for i in range(n):
            if board[i][j] == 0:
                continue

            basket.append(board[i][j])
            board[i][j] = 0
            if len(basket) >= 2 and basket[-1] == basket[-2]:
                basket.pop()
                basket.pop()
                ans += 2

            break

    return ans

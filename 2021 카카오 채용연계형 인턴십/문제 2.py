def search(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] == "P" and not check(i, j, place):
                return 0
    return 1


def check(i, j, place):
    oob = lambda i, j: i < 0 or i >= 5 or j < 0 or j >= 5
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for d in range(4):
        x, y = i + dx[d], j + dy[d]
        if not oob(x, y) and place[x][y] == "P":
            return 0

        xx = x + dx[(d + 1) % 4]
        yy = y + dy[(d + 1) % 4]
        px = i + dx[(d + 1) % 4]
        py = j + dy[(d + 1) % 4]
        if (
            not oob(xx, yy)
            and place[xx][yy] == "P"
            and (place[x][y] == "O" or place[px][py] == "O")
        ):
            return 0

        nx = x + dx[d]
        ny = y + dy[d]
        if not oob(nx, ny) and place[nx][ny] == "P" and place[x][y] == "O":
            return 0

    return 1


def solution(places):
    return [search(place) for place in places]

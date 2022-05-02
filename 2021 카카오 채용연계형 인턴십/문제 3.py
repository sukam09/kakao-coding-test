def move(dir, step):
    global cur
    if dir == "U":
        for _ in range(step):
            cur = prev[cur]
    else:
        for _ in range(step):
            cur = next_[cur]


def remove():
    global cur
    pc, nc = prev[cur], next_[cur]
    data[cur] = 0
    history.append((cur, pc, nc))

    if nc != -1:
        next_[pc] = nc
        prev[nc] = pc
        cur = nc
    else:
        next_[pc] = -1
        prev[cur] = -1
        cur = pc


def recover():
    target, pc, nc = history.pop()
    data[target] = 1

    if nc != -1:
        next_[pc] = target
        next_[target] = nc
        prev[nc] = target
        prev[target] = pc
    else:
        next_[pc] = target
        prev[target] = pc


def solution(n, k, cmd):
    global data, prev, next_, history, cur
    data = [-1] + [1] * n
    prev = [-1] + [i - 1 for i in range(1, n + 1)]
    next_ = [i + 1 for i in range(n)] + [-1]
    history = []
    cur = k + 1

    for c in cmd:
        if len(c) > 1:
            dir, step = c.split()
            move(dir, int(step))
        elif c == "C":
            remove()
        else:
            recover()

    ans = ""
    for i in range(1, n + 1):
        ans += "O" if data[i] == 1 else "X"

    return ans

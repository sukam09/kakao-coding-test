import sys
sys.setrecursionlimit(10 ** 6)


def dfs(cur, lim, left_child, right_child, num):
    global cnt
    left_num = 0
    right_num = 0
    
    if left_child[cur] != -1:
        left_num = dfs(left_child[cur], lim, left_child, right_child, num)
    if right_child[cur] != -1:
        right_num = dfs(right_child[cur], lim, left_child, right_child, num)
    
    if num[cur] + left_num + right_num <= lim:
        return num[cur] + left_num + right_num
    if num[cur] + min(left_num, right_num) <= lim:
        cnt += 1
        return num[cur] + min(left_num, right_num)
    cnt += 2
    return num[cur]


def group(root, lim, left_child, right_child, num):
    global cnt
    cnt = 0
    dfs(root, lim, left_child, right_child, num)
    cnt += 1
    return cnt


def solution(k, num, links):
    global cnt
    n = len(num)
    left_child = []
    right_child = []
    parents = [-1] * n

    for i, (left, right) in enumerate(links):
        left_child.append(left)
        right_child.append(right)
        if left != -1:
            parents[left] = i
        if right != -1:
            parents[right] = i
    
    for i, parent in enumerate(parents):
        if parent == -1:
            root = i
            break

    lo, hi = max(num), 10 ** 8
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if group(root, mid, left_child, right_child, num) <= k:
            hi = mid
        else:
            lo = mid

    return hi if lo != max(num) else lo
import sys

sys.setrecursionlimit(10**6)


def dfs(cur, lim, left_children, right_children, num):
    global cnt
    left_num = 0
    right_num = 0

    if left_children[cur] != -1:
        left_num = dfs(left_children[cur], lim, left_children, right_children, num)
    if right_children[cur] != -1:
        right_num = dfs(right_children[cur], lim, left_children, right_children, num)

    if num[cur] + left_num + right_num <= lim:
        return num[cur] + left_num + right_num
    if num[cur] + min(left_num, right_num) <= lim:
        cnt += 1
        return num[cur] + min(left_num, right_num)
    cnt += 2
    return num[cur]


def group(root, lim, left_children, right_children, num):
    global cnt
    cnt = 0
    dfs(root, lim, left_children, right_children, num)
    cnt += 1
    return cnt


def solution(k, num, links):
    global cnt
    n = len(num)
    left_children = []
    right_children = []
    parents = [-1] * n

    for i, (left_child, right_child) in enumerate(links):
        left_children.append(left_child)
        right_children.append(right_child)
        if left_child != -1:
            parents[left_child] = i
        if right_child != -1:
            parents[right_child] = i

    for i, parent in enumerate(parents):
        if parent == -1:
            root = i
            break

    start, end = max(num), 10**8
    while start + 1 < end:
        mid = (start + end) // 2
        if group(root, mid, left_children, right_children, num) <= k:
            end = mid
        else:
            start = mid

    return end if start != max(num) else start

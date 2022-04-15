import sys
sys.setrecursionlimit(10 ** 6)


def dfs(cur, lim):
    global cnt
    left_num = 0
    right_num = 0
    
    if left_child[cur] != -1:
        left_num = dfs(left_child[cur], lim)
    if right_child[cur] != -1:
        right_num = dfs(right_child[cur], lim)
    
    if nums[cur] + left_num + right_num <= lim:
        return nums[cur] + left_num + right_num
    if nums[cur] + min(left_num, right_num) <= lim:
        cnt += 1
        return nums[cur] + min(left_num, right_num)
    cnt += 2
    return nums[cur]


def group(lim):
    global cnt
    cnt = 0
    dfs(root, lim)
    cnt += 1
    return cnt


def solution(k, num, links):
    global left_child, right_child, cnt, root, nums
    n = len(num)
    left_child = []
    right_child = []
    parents = [-1] * n
    nums = num

    for i, (l, r) in enumerate(links):
        left_child.append(l)
        right_child.append(r)
        if l != -1:
            parents[l] = i
        if r != -1:
            parents[r] = i
    
    for i, p in enumerate(parents):
        if p == -1:
            root = i
            break

    lo, hi = max(nums), 10 ** 8
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if group(mid) <= k:
            hi = mid
        else:
            lo = mid

    return hi if lo != max(nums) else lo
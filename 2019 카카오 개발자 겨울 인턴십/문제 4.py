def check(mid, stones, k):
    cnt = 0
    for stone in stones:
        stone = stone - mid
        if stone < 0:
            cnt += 1
        else:
            cnt = 0
        if cnt == k:
            return False
    return True


def solution(stones, k):
    start, end = 1, max(stones) + 1
    while start + 1 < end:
        mid = (start + end) // 2
        if check(mid, stones, k):
            start = mid
        else:
            end = mid
    return start
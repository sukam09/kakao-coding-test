from heapq import heappush, heappop


def bitmask(state, idx):
    return (1 << trapidx[idx]) & state


def solution(n, start, end, roads, traps):
    global trapidx
    dists = [[float("inf")] * 1024 for _ in range(n + 1)]
    adj = [[] for _ in range(n + 1)]
    adjrev = [[] for _ in range(n + 1)]
    trapidx = [-1] * (n + 1)

    for p, q, s in roads:
        adj[p].append((q, s))
        adjrev[q].append((p, s))

    for i, t in enumerate(traps):
        trapidx[t] = i

    heap = []
    dists[start][0] = 0

    heappush(heap, (dists[start][0], start, 0))
    while heap:
        dist, idx, state = heappop(heap)
        if idx == end:
            return dist
        if dists[idx][state] < dist:
            continue

        for next_, cost in adj[idx]:
            rev = 0
            if trapidx[idx] != -1 and bitmask(state, idx):
                rev ^= 1
            if trapidx[next_] != -1 and bitmask(state, next_):
                rev ^= 1
            if rev:
                continue

            next_state = state
            if trapidx[next_] != -1:
                next_state ^= 1 << trapidx[next_]
            if dist + cost < dists[next_][next_state]:
                dists[next_][next_state] = dist + cost
                heappush(heap, (dist + cost, next_, next_state))

        for next_, cost in adjrev[idx]:
            rev = 0
            if trapidx[idx] != -1 and bitmask(state, idx):
                rev ^= 1
            if trapidx[next_] != -1 and bitmask(state, next_):
                rev ^= 1
            if not rev:
                continue

            next_state = state
            if trapidx[next_] != -1:
                next_state ^= 1 << trapidx[next_]
            if dist + cost < dists[next_][next_state]:
                dists[next_][next_state] = dist + cost
                heappush(heap, (dist + cost, next_, next_state))

from itertools import product


def solution(n, info):
    maxdiff = 1
    ans = []

    for result in product([1, 0], repeat=10):
        remain = n
        ryan = [0] * 11
        losses = []

        for i in range(10):
            if result[i] == 1:
                if remain - (info[i] + 1) < 0:
                    break
                ryan[i] = info[i] + 1
                remain -= ryan[i]

        else:
            ryan[10] += remain

            diff = 0
            for i, (a, r) in enumerate(zip(info, ryan)):
                if a == r == 0:
                    continue
                if r > a:
                    diff += 10 - i
                else:
                    diff -= 10 - i

            if diff > maxdiff:
                ans = [ryan]
                maxdiff = diff
            elif diff == maxdiff:
                ans.append(ryan)

    return sorted(ans, key=lambda x: x[::-1], reverse=True)[0] if ans else [-1]

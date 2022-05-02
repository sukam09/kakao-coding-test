from collections import defaultdict
from itertools import product


def solution(user_id, banned_id):
    candidates = defaultdict(set)
    for bid in banned_id:
        for uid in user_id:
            if len(bid) != len(uid):
                continue
            for b, u in zip(bid, uid):
                if b != "*" and b != u:
                    break
            else:
                candidates[bid].add(uid)

    results = []
    for bid in banned_id:
        results.append(candidates[bid])

    checker = set()
    for p in product(*results):
        p = frozenset(p)
        if len(p) == len(banned_id) and p not in checker:
            checker.add(p)

    return len(checker)

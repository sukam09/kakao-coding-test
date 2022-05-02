from collections import defaultdict


def solution(id_list, report, k):
    ans = []
    mail_cnt = defaultdict(int)
    report_cnt = defaultdict(int)
    reporter = defaultdict(list)

    for r in set(report):
        uid, rid = r.split()
        report_cnt[rid] += 1
        reporter[rid].append(uid)

    for rid in report_cnt:
        if report_cnt[rid] >= k:
            for uid in reporter[rid]:
                mail_cnt[uid] += 1

    for uid in id_list:
        ans.append(mail_cnt[uid])

    return ans

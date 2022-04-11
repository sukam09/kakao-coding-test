from collections import defaultdict

def solution(id_list, report, k):
    ans = []
    mail_cnt = defaultdict(int)
    report_cnt = defaultdict(int)
    reporter = defaultdict(set)
    
    for r in report:
        uid, rid = r.split()
        if uid not in reporter[rid]:
            report_cnt[rid] += 1
            reporter[rid].add(uid)
    
    for rid in report_cnt:
        if report_cnt[rid] >= k:
            for uid in reporter[rid]:
                mail_cnt[uid] += 1
    
    for uid in id_list:
        ans.append(mail_cnt[uid])
    
    return ans
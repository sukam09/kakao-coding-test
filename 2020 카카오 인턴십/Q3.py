def solution(gems):
    gem_type = len(set(gems))
    end = 0
    cur_gems = {gems[0]: 1}
    n = len(gems)
    ans = [1, n]

    for start in range(n):
        while end < n and len(cur_gems) < gem_type:
            end += 1
            if end == n:
                break
            if gems[end] in cur_gems:
                cur_gems[gems[end]] += 1
            else:
                cur_gems[gems[end]] = 1
        
        if len(cur_gems) == gem_type and end - start + 1 < ans[1] - ans[0] + 1:
            ans = [start + 1, end + 1]
        
        cur_gems[gems[start]] -= 1
        if cur_gems[gems[start]] == 0:
            del cur_gems[gems[start]]
    
    return ans
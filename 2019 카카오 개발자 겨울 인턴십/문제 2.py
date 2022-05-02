def solution(s):
    s = s.split("},{")
    for i in range(len(s)):
        if "{{" in s[i]:
            s[i] = s[i].replace("{{", "")
        if "}}" in s[i]:
            s[i] = s[i].replace("}}", "")
        s[i] = s[i].split(",")

    ans = []
    checker = {}
    s = sorted(s, key=lambda x: len(x))
    for x in s:
        for y in x:
            if y not in checker:
                ans.append(int(y))
                checker[y] = True
                break

    return ans

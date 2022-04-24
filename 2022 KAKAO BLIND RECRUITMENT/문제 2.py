def prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def solution(n, k):
    k_num = ''
    
    while n:
        k_num = str(n % k) + k_num
        n //= k
    
    k_num = k_num.split('0')
    ans = 0
    
    for kn in k_num:
        try:
            kn = int(kn)
            if prime(kn):
                ans += 1
        except:
            pass
    
    return ans
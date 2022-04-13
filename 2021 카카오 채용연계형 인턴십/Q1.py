def solution(s):
    s2i = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    for k, v in s2i.items():
        s = s.replace(k, v)
    
    return int(s)
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

    for word in s2i:
        s = s.replace(word, s2i[word])
    
    return int(s)
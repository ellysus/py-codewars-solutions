def solution(s):
    result = []
    for i in range(0, len(s), 2):
        result.append(s[i:i+2])
    
    if len(result) != 0 and len(result[-1]) != 2:
        result[-1] = result[-1] + '_'
    return result
def expanded_form(num):
    number = list(str(num))
    exp = []
    for i in range(len(number)):
        n = int(number[i]) * 10 ** (len(number) - i - 1)
        exp.append(n) if n != 0 else None
    return ' + '.join(map(str, exp))
def zeros(n):
    if n == 0: return 0
    i = 1
    while (n >= (5 ** i) and n < (5 ** (i + 1))) != True:
        i += 1
    return sum(n // (5 ** i) for i in range(1, i+1))
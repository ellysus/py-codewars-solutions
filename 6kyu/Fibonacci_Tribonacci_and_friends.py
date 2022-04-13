def Xbonacci(signature,n):
    if n == 0 or all(x <0 for x in signature):
        return []
    output = signature
    x = len(signature)
    while len(output) < n:
        output.append(sum(output[-x:]))
    return output[:n]
def tribonacci(signature, n):
    if len(signature) < 3 or n <= 0 or (signature[0] and signature[1] and signature[2]) < 0:
        return []
    output = signature
    while len(output) < n:
        output.append(output[-1] + output[-2] + output[-3])
    return output[:n]
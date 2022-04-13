def high_and_low(numbers):
    num = [int(i) for i in numbers.split()]
    return str(max(num)) + " " + str(min(num))
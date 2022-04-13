def justify(text, width):
    words = text.split()

    line = []
    output = []
    n = 0
    for w in words:

        while len(w) + n + len(line) > width:
            spaces = (len(line) - 1) or 1
            quotient, remainder = divmod(width - n, spaces)

            for i in range(spaces):
                line[i] += quotient * " " + (' ' if i < remainder else '')

            output.append(''.join(line))
            n , line = 0, []

        line.append(w)
        n += len(w)

    return '\n'.join([x.rstrip() for x in output] + [' '.join(line).ljust(width)] if line else []).rstrip()
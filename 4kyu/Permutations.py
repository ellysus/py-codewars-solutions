import itertools

def permutations(input):
    return list(set([''.join(x) for x in itertools.permutations(input)]))
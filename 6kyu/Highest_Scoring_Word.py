def high(string):
    scores = {}
    for word in string.lower().split():
        score = sum(ord(x) - 96 for x in word)
        scores[word] = score
    #return the word with the highest score
    return max(scores, key=scores.get)
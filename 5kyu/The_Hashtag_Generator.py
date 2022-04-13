def generate_hashtag(s):
    return False if len(s) == 0 or len(s.split()[0]) > 140 else '#' + ''.join(word.capitalize() for word in s.split())
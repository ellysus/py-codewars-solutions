def alphabet_position(text):
    out=[]
    chars = list(text.lower())
    for char in chars:
        if char.isalpha():
            out.append(ord(char) - 96)
    return ' '.join(map(str, out))
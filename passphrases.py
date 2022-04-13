def passphrases(string, shift:int):
    string = string.lower()
    cipher = ""
    for i in range(len(string)):
        if string[i].isalpha():
            cipher += chr((ord(string[i]) + shift - 97) % 26 + 97).upper() if i % 2 == 0 else chr((ord(string[i]) + shift - 97) % 26 + 97)
        elif string[i].isdigit():
            cipher += str(9 - int(string[i]))
        else:
            cipher += string[i]

    return ''.join(reversed(list(cipher)))

def swap(string_):
    return "".join([x.upper() if x == x.lower() else x.lower() for x in string_])

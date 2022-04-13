def create_phone_number(n):
    return f"({''.join(str(x) for x in n[0:3])}) {''.join(str(x) for x in n[3:6])}-{''.join(str(x) for x in n[6:])}"
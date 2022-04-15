def next_bigger(n):
    digits = list(str(n))
    
    #find piv
    pivot = -1
    for i in range(len(digits)-1, 0, -1):
        if int(digits[i]) > int(digits[i-1]):
            pivot = digits[i-1]
            break
    
    #If no piv
    if pivot == -1: return -1

    #right side of the number
    right = digits[i:]

    mm,mmi = None,None
    for j in range(len(right)):
        if int(right[j]) > int(pivot):
            if mm == None or int(mm) > int(right[j]):
                mm = right[j]
                mmi = j

    if mmi == None: return -1
    
    right.remove(mm)
    right.append(pivot)
    new_right = sorted(right)
    left = digits[:i-1]
    return int(''.join(left + [mm] + new_right))
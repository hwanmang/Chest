result = ""
    for i in my_string:
        if i in alp:
            result += i.upper()
        else:
            result += i
    return result
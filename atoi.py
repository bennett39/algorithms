def atoi(s):
    #  return int(s)
    output = 0
    for c in s:
        if not c.isdigit():
            raise TypeError
        output *= 10
        output += int(c)
    return output

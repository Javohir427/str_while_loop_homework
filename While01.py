def main(s):
    """
    A variable of type str is given. Find how many numbers it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    
    n = 0
    i = 0
    # return s[4]
    
    while i < len(s) :
        if s[i].isdigit():
         n += 1
        i += 1
    return n

print(main('12366wed'))


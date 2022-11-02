def main(s):
    """
    A variable of type str is given. Find how many letters it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    n = 0
    i = 0
   
    
    while i < len(s) :
        if s[i].isdigit():
         n += 1
        i += 1
    return len(s)-n


print(main('r4gt456'))
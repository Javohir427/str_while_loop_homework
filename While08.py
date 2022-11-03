def main(s):
    """
    A string of numbers is given. Find how many odd numbers there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0
    n = 0
    while i < len(s):
        if s[i].isdigit():
            if int(s[i])%2==1:
                n+=1
            else:
                n+=0
        i+=1
    return n
print(main("1567534"))
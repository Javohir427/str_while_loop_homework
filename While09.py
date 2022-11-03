def main(s):
    """
    A string of numbers is given. Find the sum of all the numbers and return.
    Args:
        s: str
    Returns:
        int: return answer
    """


    i = 0
    n = 0
    while i<len(s):
        if ((s[i])).isdigit():  
            n+=int(s[i])
        else:
            n+=0
        i+=1
    return n

print(main("987654"))            

      
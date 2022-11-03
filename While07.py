def main(s):
    """
    A string of numbers is given. Find how many even numbers there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0
    n = 0
    while i<len(s):
        if (s[i]).isdigit():
            if int(s[i])%2==0 :
                n+=1
            else  :
                n+=0
            
        i+=1
    return n
print(main("56786543250"))
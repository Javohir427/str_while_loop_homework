def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd numbers.
    Args:
        s: str
    Returns:
        int: return answer
    """
    
    i = 0
    n = 0
    while i<len(s):
        if s[i].isdigit():
            if int(s[i])%2==1:
                n+=int(s[i])
            else :
                n+=0
        i+=1
    return n 
print(main("98421"))


        
            
            


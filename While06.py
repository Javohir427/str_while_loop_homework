def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    i = 0
    n = 0
    
    while i<len(s):
        if (s[i]).isalpha():

            if (s[i])=='a' or (s[i])=='e' or (s[i])=='i' or (s[i])=='o' or (s[i])=='u' or (s[i])=='A' or (s[i])=='E' or (s[i])=='I' or (s[i])=='O' or (s[i])=='U':
                n+=0
             
            else :
                n+=1
        i+=1

    return n  
print(main("CodeschoolUz")) 

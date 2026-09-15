def is_palindrome_valid(s: str) -> bool:    
    # Write your code here
    #String to char array
    str_arr = list(s)
    #print('str arr',str_arr)
    #remove non alpha numeric
    alpha_numeric_arr = []
    for c in str_arr:
        #print('c',c)
        if c.isalpha() or c.isnumeric():
            #print('c is alpha numeric',c)
            alpha_numeric_arr += [c.lower()]
    #print('alpha-numeric-arr',alpha_numeric_arr)     
    left = 0
    right = len(alpha_numeric_arr)-1
    while left < right:
        if alpha_numeric_arr[left] == alpha_numeric_arr[right]:
            left+=1
            right-=1
            continue
        else:
            return False        
    return True


def main(): 
    test_cases = [
        "a dog! a panic in a pagoda.",
        "A man, a plan, a canal: Panama",
        "abc123"]
    for s in test_cases:
        print(f"{s} -> {is_palindrome_valid(s)}")

if __name__ == "__main__":
    main()

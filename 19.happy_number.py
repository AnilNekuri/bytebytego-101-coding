def happy_number(n: int) -> bool:
    # Write your code here

    fast: int = n
    slow: int = n
    while True:

        fast = generate_sum_sq_digits(generate_sum_sq_digits(fast))
        slow = generate_sum_sq_digits(slow)
        
        if fast == 1:
            return True
        elif fast == slow:
            return False
    return False
    
def generate_sum_sq_digits(n: int) -> int:
    x = n
    sum_sq_digits = 0
    while x != 0:
        r = x%10
        sum_sq_digits += (r * r)
        x = x//10
    
    return sum_sq_digits

if __name__ == "__main__":
    result: bool = happy_number(19)
    print('result',result)

# 23 = 4 + 9 = 13 
# 1 + 9 = 10
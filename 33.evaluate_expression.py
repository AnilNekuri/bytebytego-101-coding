def evaluate_expression(s: str) -> int:
    # Write your code here
    stack: str = []
    char_list = list(s)
    i = 0
    while i < len(char_list):
        if char_list[i] == ')':
            val: int = 0
            while stack[-1] != '(':
                sub_val: int = 0
                if isinstance(stack[-1], int):
                    sub_val = stack.pop()
                    if stack and (stack[-1] == '-' or stack[-1] == '+'):
                        sub_val = -sub_val if stack.pop() == "-" else sub_val
                    val += sub_val
            stack.pop()
            stack.append(val)
            i+=1
            continue


        if not char_list[i].isdigit():
            stack.append(char_list[i])
            i=i+1
            continue
        number = 0
        while i < len(char_list) and char_list[i].isdigit():
            number = 10 * number + int(char_list[i])
            i=i+1
        stack.append(number)
    result: int = 0
    sign: int = 1
    for s in stack:
        if s == '-':
            sign= -1
        if s == '+':
            sign= +1
        if isinstance(s,int):
            result += (int(s)*sign)
    return result

if __name__ == "__main__":
    result = evaluate_expression("18-(7+(2-4+()))")
    print("result",result)
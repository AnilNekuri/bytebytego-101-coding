def valid_parenthesis_expression(s: str) -> bool:
    parenthesis_map = { '(':')', '[':']', '{':'}'}
    stack = []
    for c in s:
        if c in parenthesis_map:
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            top_c = stack[-1]
            if parenthesis_map[top_c] == c:
                stack.pop()
            else:
                return False
    # Write your code here
    return True if len(stack) == 0 else False

if __name__ == "__main__":
    result = valid_parenthesis_expression("([]{})")
    print('result',result)
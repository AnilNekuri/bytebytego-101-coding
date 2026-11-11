def repeated_removal_of_adjacent_duplicates(s: str) -> str:
    # Write your code here
    char_arr = list(s)
    stack = []
    for c in char_arr:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    return ''.join(stack)

if __name__ == "__main__":
    result = repeated_removal_of_adjacent_duplicates(s="aacabba")
    print('result: ',result)
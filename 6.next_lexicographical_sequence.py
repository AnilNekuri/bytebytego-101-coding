def next_lexicographical_sequence(s: str) -> str:
    # Write your code here
    if len(s) < 2:
        return s
    #String to char list
    char_arr = list(s)  
    #Find incremental pivot
    pivot_index = -1
    for i in range(len(char_arr)-2,-1,-1):
        if char_arr[i] >= char_arr[i+1]:
            continue
        pivot_index = i
        break
    print('pivot_index',pivot_index)
    #swap pivot to next char from the right
    if pivot_index >= 0:
        swap_index = len(s)-1
        for i in range(len(char_arr)-1,pivot_index,-1):
            if char_arr[pivot_index] < char_arr[i]:
                swap_index = i
                break
        temp = char_arr[swap_index]
        char_arr[swap_index] = char_arr[pivot_index]
        char_arr[pivot_index] = temp 
    #reverse the non incremental after pivot position
    swap_count = int((len(s) - (pivot_index+1))/2)
    for i in range(swap_count):
        temp = char_arr[pivot_index+1+i]
        char_arr[pivot_index+1+i] = char_arr[len(s)-1-i]
        char_arr[len(s)-1-i] = temp
        
    return "".join(char_arr)
if __name__ == "__main__":
    test_cases = [
        "abcedda",
        # "bb",
        # "hefg",
        # "dhck",
        # "dkhc"
    ]
    for test in test_cases:
        print('next_lexicographical_sequence',test,next_lexicographical_sequence(test))
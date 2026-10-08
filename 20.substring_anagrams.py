def substring_anagrams(s: str, t: str) -> int:
    result = 0
    window_freq = [0 for _ in range(26)]
    expected_freq = [0 for _ in range(26)]
    #print(window_freq)
    #Fill expected freq
    for c in list(t):
        expected_freq[ord(c)-ord('a')] += 1 

    len_s = len(s)
    len_t = len(t)
    if len_t > len_s or len_t == 0:
        return 0
    for index in range(len_t):
        c = s[index]
        window_freq[ord(c)-ord('a')] += 1 
    if compare_fre(window_freq,expected_freq):
        result += 1

    left_index = 0
    right_index = len_t - 1
    while right_index < len_s-1:
        window_freq[ord(s[left_index])-ord('a')] -= 1
        left_index += 1
        right_index += 1
        window_freq[ord(s[right_index])-ord('a')] += 1
        if compare_fre(window_freq,expected_freq):
            result += 1
    
    print(expected_freq)
    return result

def compare_fre(window_freq:list, expected_freq:list):
    
    for index in range(26):
        if window_freq[index] != expected_freq[index]:
            return False
    return True

if __name__ == "__main__":
    s = "caabab"
    t = "aba"
    result = substring_anagrams(s=s, t=t)
    print('result',result)
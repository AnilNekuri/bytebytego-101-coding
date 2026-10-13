def longest_uniform_substring_after_replacements(s: str, k: int) -> int:
    # Write your code here
    result = 0
    max_freq = 0
    left = right = 0
    len_s = len(s)
    freq = {}
    while right < len_s:
        c = s[right]
        freq[c] = freq.get(c,0) + 1
        max_freq = max(max_freq,freq[c])
        len_window = right - left + 1
        if k >= len_window - max_freq:
            result = max(result,len_window)
        else:
            freq[s[left]] = freq.get(s[left]) - 1
            left += 1
        right += 1

    return result 

if __name__ == "__main__":
    s = "AABCDCCA"
    k = 2
    result = longest_uniform_substring_after_replacements(s=s,k=k)
    print('result',result)

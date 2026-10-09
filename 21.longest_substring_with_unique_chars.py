def longest_substring_with_unique_chars(s: str) -> int:
   result = 0
   memory = set()
   right = 0
   left = 0
   len_s = len(s)
   while right < len_s:
      if s[right] in memory:
        while s[left] != s[right]:
           left+=1
        left+=1

      else:
        result = max(result,(right-left)+1)
        memory.add(s[right])
      right+=1
   return result

if __name__ == "__main__":
   result:int = longest_substring_with_unique_chars("abcba")
   print('result',result)
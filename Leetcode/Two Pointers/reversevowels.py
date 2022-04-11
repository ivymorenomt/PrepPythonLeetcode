def reverseVowel(s):
    l = 0
    r = len(s) - 1
    lst = list(s)
    
    while l < r:
        if lst[l] not in "aeiouAEIOU":
            l+=1 # skip if it isn't a vowel
        elif lst[r] not in "aeiouAEIOU":
            r-=1
        else:
            lst[l], lst[r] = lst[r], lst[l]
            l+=1
            r-=1
    return "".join(lst)
            
s = "leetcode"
print(reverseVowel(s))
import string
def isPalindrome(s):
    print(s)
    s = ''.join(ch for ch in s if ch.isalnum()).lower()
    print(s)
    return s == s[::-1]
    
    
s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))
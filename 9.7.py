def isPalindrome(String):
    String=String.strip().upper()
    
    if isinstance(String,str) and String[::-1]==String:
        return "Given String is Palindrome"
    
    else:
        return "Given string is not Palindrome"
    
print(isPalindrome("  maDaM    "))

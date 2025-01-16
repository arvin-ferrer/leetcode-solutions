def isPalindrome(x):
    string = str(x)
    reverse = string[::-1]    
    if string == reverse:
        return True
    return False

print(isPalindrome("121"))

def isPalindrome(string):
	if string == string[::-1]:
        return True
    else:
        return False

print(isPalindrome('aza'))
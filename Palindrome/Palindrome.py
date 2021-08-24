# function which return reverse of a string

def isPalindrome(s):
    return s == s[::-1]


# Driver code
s = "malayalam"
ans = isPalindrome(s)

If (ans):
    print("Yes")
else:
    print("No")
